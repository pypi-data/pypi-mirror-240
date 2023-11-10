# (2022) On Embeddings for Numerical Features in Tabular Deep Learning<!-- omit in toc -->

- [Usage](#usage)
- [End-to-end examples](#end-to-end-examples)
- [Practical notes](#practical-notes)
- [API](#api)

# Usage

> [!IMPORTANT]
> It is recommended to first read the TL;DR of the paper:
> [link](https://github.com/yandex-research/tabular-dl-num-embeddings#tldr)

Let's consider a toy tabular data problem where objects are represented by three
continuous features
(for simplicity, other feature types are omitted,
but they are covered in the end-to-end example):

<!-- test main -->
```python
# NOTE: all code snippets can be copied and executed as-is.
import torch
import torch.nn as nn
from rtdl.num_embeddings import (
    LinearReLUEmbeddings,
    PeriodicEmbeddings,
    PiecewiseLinearEncoding,
    PiecewiseLinearEmbeddings,
    compute_bins,
)
from rtdl.revisiting_models import MLP

batch_size = 256
n_cont_features = 3
x = torch.randn(batch_size, n_cont_features)
```

This is how a vanilla MLP **without embeddings** would look like:

<!-- test main -->
```python
mlp_config = {
    'd_out': 1,  # For example, a single regression task.
    'n_blocks': 2,
    'd_block': 256,
    'dropout': 0.1,
}
model = MLP(d_in=n_cont_features, **mlp_config)
y_pred = model(x)
```

And this is how MLP **with embeddings for continuous features** can be created:

<!-- test main -->
```python
d_embedding = 24
m_cont_embeddings = PeriodicEmbeddings(n_cont_features, lite=False)
model_with_embeddings = nn.Sequential(
    # Input shape: (batch_size, n_cont_features)

    m_cont_embeddings,
    # After embeddings: (batch_size, n_cont_features, d_embedding)

    # NOTE: `nn.Flatten` is not needed for Transformer-like architectures.
    nn.Flatten(),
    # After flattening: (batch_size, n_cont_features * d_embedding)

    MLP(d_in=n_cont_features * d_embedding, **mlp_config)
    # The final shape: (batch_size, d_out)
)
# The usage is the same as for the model without embeddings:
y_pred = model_with_embeddings(x)
```

In other words, the whole paper is about the fact that having such a thing as
`m_cont_embeddings` can (significantly) improve the downstream performance,
and the paper showcases three types of such embeddings:
simple, periodic and piecewise-linear.

## Simple LR embeddings<!-- omit in toc -->

*(Decribed in Section 3.4 in the paper)*

| Name | Definition for a single feature | How to create               |
| :--- | :------------------------------ | :-------------------------- |
| `LR` | `ReLU(Linear(x_i))`             | `LinearReLUEmbeddings(...)` |

In the above table:
- L ~ Linear, R ~ ReLU.
- `x_i` is the i-th scalar continuous feature

**Hyperparameters**

- The default value of `d_embedding` is set with the MLP backbone in mind.
  Typically, for Transformer-like backbones, the embedding size is larger.
- On most tasks, tuning `d_embedding` will not have much effect.
- See other notes on hyperparameters in ["Practical notes"](#practical-notes).

<!-- test main _ -->
```python
# MLP-LR
d_embedding = 32
model = nn.Sequential(
    LinearReLUEmbeddings(n_cont_features, d_embedding),
    nn.Flatten(),
    MLP(d_in=n_cont_features * d_embedding, **mlp_config)
)
y_pred = model(x)
```

## Periodic embeddings<!-- omit in toc -->

*(Decribed in Section 3.3 in the paper)*

| Name        | Definition for a single feature     | How to create                                           |
| :---------- | :---------------------------------- | :------------------------------------------------------ |
| `PLR`       | `ReLU(Linear(Periodic(x_i)))`       | `PeriodicEmbeddings(..., lite=False)`                   |
| `PLR(lite)` | `ReLU(SharedLinear(Periodic(x_i)))` | `PeriodicEmbeddings(..., lite=True)`                    |
| `PL`        | `Linear(Periodic(x_i))`             | `PeriodicEmbeddings(..., activation=False, lite=False)` |

In the above table:
- P ~ Periodic, L ~ Linear, R ~ ReLU.
- `x_i` is the i-th scalar continuous feature
- `Periodic(x_i) = concat[cos(h_i), sin(h_i)]`, where:
  - `h_i = 2 * pi * Linear(x_i, bias=False)`
  - `h_i.shape == (k,)` (`k` is a hyperparameter)
- `lite` is a new option introduced in
  [TabR](https://github.com/yandex-research/tabular-dl-tabr/).
  On some tasks, it allows making the `PLR` embedding *significantly* more lightweight
  at the cost of non-critical performance loss.

**Hyperparameters**

- <details><summary><b>How to tune the <code>sigma</code> hyperparameter</b></summary>

  **Prioritize testing smaller values, because they are safer:**
  - Larger-than-the-optimal value can lead to terrible performance.
  - Smaller-than-the-optimal value will still yield decent performance.

  Some approximate numbers:
  - for 30% of tasks, the optimal `sigma` is less than 0.05.
  - for 50% of tasks, the optimal `sigma` is less than 0.2.
  - for 80% of tasks, the optimal `sigma` is less than 1.0.
  - for 90% of tasks, the optimal `sigma` is less than 5.0.

  If you want to test larger values,
  make sure that you have enough hyperparameter tuning budget
  (e.g. at least 100 trials of the TPE Optuna sampler, as in the paper).

  </details>

- The default value of `d_embedding` is set with the MLP backbone in mind.
  Typically, for Transformer-like backbones, the embedding size is larger.

- See other notes on hyperparameters in ["Practical notes"](#practical-notes).

<!-- test main _ -->
```python
# Example: MLP-PLR
d_embedding = 24
model = nn.Sequential(
    PeriodicEmbeddings(n_cont_features, d_embedding, lite=False),
    nn.Flatten(),
    MLP(d_in=n_cont_features * d_embedding, **mlp_config)
)
y_pred = model(x)
```

## Piecewise-linear encoding & embeddings<!-- omit in toc -->

*(Decribed in Section 3.2 in the paper)*

<img src="piecewise-linear-encoding.png" width=90%>

| Name                                | Definition for a single feature | How to create                                      |
| :---------------------------------- | :------------------------------ | :------------------------------------------------- |
| `Q`/`T` (only for MLP-like models!) | `ple(x_i)`                      | `PiecewiseLinearEncoding(bins)`                    |
| `QL`/`TL`                           | `Linear(ple(x_i))`              | `PiecewiseLinearEmbeddings(bins)`                  |
| `QLR` / `TLR`                       | `ReLU(Linear(ple(x_i)))`        | `PiecewiseLinearEmbeddings(bins, activation=True)` |

In the above table:
- Q/T ~ quantiles-/tree- based bins, L ~ Linear, R ~ ReLU.
- `x_i` is the i-th scalar continuous feature.
- `ple` stands for "Piecewise-linear encoding".

**Notes**

- The output of `PiecewiseLinearEncoding` has the shape `(*batch_dims, d_encoding)`,
  where `d_encoding` equals the total number of bins of all features.
  This is the most lightweight variation of piecewise-linear representations
  without trainable parameters suitable only for MLP-like models.
- By contrast, `PiecewiseLinearEmbeddings` is similar to all other classes of
  this package and its output has the shape `(*batch_dims, n_features, d_embedding)`.

**Hyperparameters**

- See other notes on hyperparameters in ["Practical notes"](#practical-notes).

<!-- test main _ -->
```python
X_train = torch.randn(10000, n_cont_features)
Y_train = torch.randn(len(X_train))  # Regression.

# (Q) Quantile-based bins.
bins = compute_bins(X_train)
# (T) Target-aware (tree-based) bins.
bins = compute_bins(
    X_train,
    # NOTE: requires scikit-learn>=1.0 to be installed.
    tree_kwargs={'min_samples_leaf': 64, 'min_impurity_decrease': 1e-4},
    y=Y_train,
    regression=True,
)

# MLP-Q / MLP-T
model = nn.Sequential(
    PiecewiseLinearEncoding(bins),
    nn.Flatten(),
    MLP(d_in=sum(len(b) - 1 for b in bins), **mlp_config)
)
y_pred = model(x)

# MLP-QL / MLP-TL
model = nn.Sequential(
    PiecewiseLinearEmbeddings(bins, d_embedding),
    nn.Flatten(),
    MLP(d_in=n_cont_features * d_embedding, **mlp_config)
)
y_pred = model(x)
```

# End-to-end examples

See [this Jupyter notebook](./example.ipynb).

# Practical notes

**General comments**

- **Embeddings for continuous features are applicable to most tabular DL models**
  and often lead to better task performance.
  On some problems, embeddings can lead to truly significant improvements.
- As of 2022-2023, **MLP with embeddings is a good modern baseline**
  in terms of both task performance and efficiency.
  Depending on the task and embeddings, it can perform on par or even better than
  FT-Transformer, while being significantly more efficient.
- Despite the formal overhead in terms of parameter count,
  **embeddings are perfectly affordable in many cases**.
  That said, on big enough datasets and/or with large enough number of features and/or
  with strict enough latency requirements,
  the new overhead associated with embeddings may become an issue.

**What embeddings to use in practice?**

*(this section assumes MLP as the backbone)*

- `LinearReLUEmbeddings`
  - Falls into the "low risk & low reward" category.
  - The most lightweight thing in this package.
  - Good choice for a quick start on a new problem, especially if 
    this is your first time working with embeddings.
- `PeriodicEmbeddings`
  - Demonstrates the best performance on average.
  - On some problems, `lite=True` can make the embeddings significantly
    more lightweight at the const of non-critical performance loss.
- `PiecewiseLinearEncoding` & `PiecewiseLinearEmbeddings`
  - Can produce good results on some datasets.
  - To test whether piecewise-linear representations are beneficial
    for your task, start with MLP + `PiecewiseLinearEncoding`.
    If you like the results, try `PiecewiseLinearEmbeddings`.

**Hyperparameters**

> [!NOTE]
> It is possible to explore tuned hyperparameters
> for the models and datasets used in the paper as explained here:
> [here](https://github.com/yandex-research/tabular-dl-num-embeddings#how-to-explore-metrics-and-hyperparameters).

- The default hyperparameters are set with the MLP-like backbones in mind and
  with "low risk" (not the "high reward") as the priority.
  For Transformer-like models, one may want to significantly increase `d_embedding`.
- For MLP-like models, for embeddings ending with a linear layer `L`
  (e.g. `LRL`, `PL`, etc.)
  a safe default stratagy is to set `d_embedding` to a small value.
  The hidden dimension (`d_hidden` for `SimpleEmbeddings`, `k` for `PeriodicEmbeddings`,
  `n_bins` for `PiecewiseLinearEmbeddings`),
  in turn, usually can be safely set to a relatively large value.
- For MLP-like models, for embeddings ending with a ReLU-like activation
  (`LR`, `PLR`, etc.), `d_embedding` may need (significantly) larger values
  than the default one.
- Tuning hyperparameters of the periodic embeddings can require special considerations
  as described in the [corresponding usage section](#periodic-embeddings).
- In the paper, for hyperparameter tuning, the
  [TPE sampler from Optuna](https://optuna.readthedocs.io/en/stable/reference/samplers/generated/optuna.samplers.TPESampler.html)
  was used with `study.optimize(..., n_trials=100)` (sometimes, `n_trials=50`).
- The hyperparamer tuning spaces can be found in the appendix of the paper
  and in `exp/**/*tuning.toml` files in the repository reproducing the paper.

**Tips**

- To improve efficiency, it is possible to embed only a subset of features.
- The biggest wins come from embedding *important, but "problematic"* features
  (intuitively, it means features with irregular
  joint distributions with other (important) features and labels).
- It is possible to combine embeddings and apply different embeddings to different features.
- The proposed embeddings are relevant only for continuous features,
  so they should not be used for embedding binary or categorical features.
- If an embedding ends with a linear layer (`PL`, `QL`, `TL`, `LRL`) and its output
  is passed to MLP, then that linear layer can be fused with the first linear layer of
  MLP after the training (sometimes, it can lead to better efficiency).
- (a bonus tip for those who read such long documents until the end)
  On some problems, MLP-L
  (that is, MLP with `rtdl.revisiting_models.LinearEmbeddings` -- the simplest possible
  linear embeddings) performs better than MLP.
  Combined with the previous bullet, it means that on some problems,
  one can train MLP-L and transform it to a simple embedding-free MLP after the training.

# API

[This note](../../README.md#api) explains how to explore the formal API and docstrings.

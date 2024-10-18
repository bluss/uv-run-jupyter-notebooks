#!/usr/bin/env -S JUPYTER_CONFIG_DIR=jupyter uv run --with jupyterlab,jupytext jupyter-lab
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     notebook_metadata_filter: title
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   title: Hey
# ---

# %% [markdown]
# ## `uv run` notebook with dependencies in shebang

# %%
import sys
sys.prefix, sys.version_info

# %%
# dependencies
# !uv pip install "seaborn>=0.13"

# %%
import seaborn as sns

# %%
df = sns.load_dataset("penguins")

# %%
sns.pairplot(data=df, hue="species");

# %%

# %%

# %%

#!/usr/bin/env -S uv run --script
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
#   title: Self-starting jupytext inline script dependencies notebook
# ---

# %%
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "notebook>=7.2",
#     "jupytext>=1.16.0",
#     "seaborn>=0.13",
# ]
# ///

# %% jupyter={"source_hidden": true}
def _start_notebook_if_needed():
    import os
    # check if we are already in jupyter
    # JPY_PARENT_PID set by jupyter-client, VSCODE_PID set by by vscode
    if os.environ.get("JPY_PARENT_PID", "") or os.environ.get("VSCODE_PID", ""):
        return
    # start current file -- with an url and query string
    import urllib.parse
    import notebook.app
    url_arg = '--JupyterNotebookApp.default_url='
    url_arg += "/notebooks/" + urllib.parse.quote(os.path.basename(__file__)) + "?factory=Notebook"
    notebook.app.launch_new_instance(argv=[url_arg])
    raise SystemExit(0)
_start_notebook_if_needed()

# %% [markdown]
# ## `uv run --script` jupytext notebook with embedded dependencies

# %%
import sys
sys.prefix, sys.version_info

# %%
import seaborn as sns

# %%
df = sns.load_dataset("penguins")

# %%
sns.pairplot(data=df, hue="species");

# %%


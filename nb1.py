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
#   title: Hey
# ---

# %%
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "jupyterlab>=4.2",
#     "jupytext>=1.16.0",
#     "seaborn>=0.13",
# ]
# ///

# %% [markdown]
# ## `uv run --script` jupytext notebook with embedded dependencies
# %%
def _start_jupyterlab():
    "start this file in jupyterlab (if not already there)"
    import os
    # check if we are already in jupyterlab
    if __name__ != "__main__" or os.environ.get("JPY_SESSION_NAME", ""):
        return
    import signal
    import subprocess
    # turn off Ctrl-C for this particular process
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # setup the jupytext configuration
    environment = os.environ.copy()
    environment["JUPYTER_CONFIG_DIR"] = "jupyter"
    subprocess.run(["jupyter-lab", __file__], check=True, env=environment)
    raise SystemExit(0)
_start_jupyterlab()

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


# %%

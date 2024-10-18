
# Can We Embed Dependencies Directly into a Jupyter Notebook?

Let's use uv to try to do this.

## How to Run the Examples

The notebooks are executable and they use **uv** to run.

You can run them like this:

`uv run --script nb1.py`
`./nb2.py`

## `nb1.py`

`nb1.py` uses a [PEP 723](https://peps.python.org/pep-0723/) metadata
and lets `uv run --script` read it.

But we need to add another function into the script itself that starts
Jupyterlab. This could still be the best solution, because dependencies are
clearly declared in the file.

It's nice to see that `jupytext` notebook metadata and the script metadata
coexists, and is preserved correctly when editing the notebook in Jupyterlab.


## `nb2.py`

`nb2.py` just uses a shebang to run jupyter-lab directly with the text
notebook. This works because jupytext is installed. But the workaround
mentioned below needs to be applied here too, unfortunately, if you're
not already a jupytext user.

The shebang is preserved correctly when editing the notebook in Jupyterlab,
but it's not visible for editing in the notebook interface.

This notebook just uses uv directly in the notebook to add the remaining
notebook dependencies. Which we can do if we know uv is available.


## Jupytext and Plain `.py` Notebooks

Jupytext is a jupyter extension that enables notebooks to be saved as plaintext
Python files, which is very useful for many projects. The examples here make
sure to install Jupytext so that Jupyterlab opens our .py notebooks directly.

An unfortunate override is needed for Jupytext - we need to configure Jupyterlab
so that it opens .py files as notebooks. Normally a Jupytext user will have
already done this configuration, but here we want to enable it by force and
automatically. That's why there is a thing to set `JUPYTER_CONFIG_DIR` in
`nb1.py`.

To avoid this problem, you can just run and set this config for your user in
general:

```
uvx --from jupytext jupytext-config set-default-viewer python
```

but note that this changes your default viewer for python files - not a good
idea if you don't normally use jupytext. (But you should!)

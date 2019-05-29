# alabaster-jupyterhub

[![PyPI version](https://badge.fury.io/py/alabaster_jupyterhub.svg)](https://badge.fury.io/py/alabaster_jupyterhub)

A Sphinx theme used by the JupyterHub org projects. It is a slight modification
of the Alabaster theme.

## Installation

```
pip install alabaster_jupyterhub
```

## Configuration

In `conf.py`, add the following lines:

```
import alabaster_jupyterhub

...

html_theme = 'alabaster_jupyterhub'
html_theme_path = [alabaster_jupyterhub.get_html_theme_path()]

...

# If you have a RTD check, make sure to set theme
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    html_theme = 'alabaster_jupyterhub'
    html_theme_path = [alabaster_jupyterhub.get_html_theme_path()]
```

## Customization

If you'd like to add an `Edit with GitHub` section to each
page, add the following configuration to your `conf.py` file,
along with the proper configuration for your repository:

```python
html_context = {
    # The GitHub org for this repo
    "github_user": "jupyterhub",
    # The GitHub repository
    "github_repo": "alabaster-jupyterhub",
    # The branch from which you host documentation
    "github_version": "master",
    # The path (relative to root) for your documentation
    "doc_path": "doc",  
}
```

# alabaster-jupyterhub

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

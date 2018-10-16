"""The JupyterHub Alabaster theme"""
import os

from alabaster_jupyterhub import _version as version

__version__ = version.__version__

with open(os.path.join(os.path.dirname(__file__), "_version.py")) as fp:
    exec(fp.read(), None, {})

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("alabaster_jupyterhub", theme_path)
    return {"version": version.__version__, "parallel_read_safe": True}

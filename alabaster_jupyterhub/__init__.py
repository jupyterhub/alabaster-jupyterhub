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

def get_html_theme_path():
    """
    Utility to return theme location.
    Used in Sphinx conf.py to set html_theme_path.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def setup(app):
    app.add_html_theme('alabaster_jupyterhub', os.path.abspath(os.path.dirname(__file__)))

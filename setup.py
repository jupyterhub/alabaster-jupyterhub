#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("alabaster_jupyterhub/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(
    name="alabaster_jupyterhub",
    version=version,
    description="A configurable sidebar-enabled Sphinx theme for Project Jupyter",
    author="Project Jupyter",
    author_email="jupyter@googlegroups.org",
    url="https://github.com/jupyterhub/alabaster-jupyterhub",
    packages=["alabaster_jupyterhub"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["alabaster_jupyterhub = alabaster_jupyterhub"]},
    install_requires=[
       'sphinx',
       'alabaster',
    ]
)

====================
Alabaster-JupyterHub
====================

Ths is a lightweight extension of the excellent `Alabaster theme <https://alabaster.readthedocs.io/en/latest/>`_
for Sphinx, for use with the JupyterHub projects.

This is a demo for the changes we make to the Alabaster theme. If
any new changes are added, we can preview them here. Anything that's *not*
explicitly demoed should be assumed to be the same as the Alabaster theme.

Modifying the sidebar and body captions 
=======================================

We often use the ``toctree`` "caption" argument to add a small caption header
to toc lists. This adds a section break in the side bar as well as a short
header above the TOC. We'd like these to look more like "titles" instead of
in-line captions.

.. toctree::
   :caption: This is the first caption

   foo <https://jupyter.org/>
   bar <https://jupyter.org/>

.. toctree::
   :caption: And now, the second caption
   :maxdepth: 1

   foo <https://jupyter.org/>
   bar <https://jupyter.org/>

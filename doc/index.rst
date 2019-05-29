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
   :maxdepth: 2

   page2
   page3

.. toctree::
   :caption: And now, the second caption
   :maxdepth: 1

   foo <https://jupyter.org/>
   bar <https://jupyter.org/>


Lorem Ipsum
===========

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget ipsum blandit,
tristique velit quis, aliquam libero. Sed vitae accumsan tortor, vitae vulputate tellus.
Sed sed lacus mauris. Duis efficitur, tellus maximus fermentum faucibus, tellus sapien
ornare arcu, ac vulputate ante erat a arcu. Praesent maximus nisl eget est tincidunt,
non suscipit metus volutpat. Quisque volutpat lectus id arcu volutpat molestie. Integer
tincidunt lorem et lobortis cursus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget ipsum blandit,
tristique velit quis, aliquam libero. Sed vitae accumsan tortor, vitae vulputate tellus.
Sed sed lacus mauris. Duis efficitur, tellus maximus fermentum faucibus, tellus sapien
ornare arcu, ac vulputate ante erat a arcu. Praesent maximus nisl eget est tincidunt,
non suscipit metus volutpat. Quisque volutpat lectus id arcu volutpat molestie. Integer
tincidunt lorem et lobortis cursus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget ipsum blandit,
tristique velit quis, aliquam libero. Sed vitae accumsan tortor, vitae vulputate tellus.
Sed sed lacus mauris. Duis efficitur, tellus maximus fermentum faucibus, tellus sapien
ornare arcu, ac vulputate ante erat a arcu. Praesent maximus nisl eget est tincidunt,
non suscipit metus volutpat. Quisque volutpat lectus id arcu volutpat molestie. Integer
tincidunt lorem et lobortis cursus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget ipsum blandit,
tristique velit quis, aliquam libero. Sed vitae accumsan tortor, vitae vulputate tellus.
Sed sed lacus mauris. Duis efficitur, tellus maximus fermentum faucibus, tellus sapien
ornare arcu, ac vulputate ante erat a arcu. Praesent maximus nisl eget est tincidunt,
non suscipit metus volutpat. Quisque volutpat lectus id arcu volutpat molestie. Integer
tincidunt lorem et lobortis cursus.
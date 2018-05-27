.. {{ cookiecutter.project_slug }} documentation master file, created by
   sphinx-quickstart on Tue Jul  9 22:26:36 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.project_name }}'s documentation!
{{ '=' * (28 + cookiecutter.project_name | length) }}

Contents:

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   Project structure <modules>
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

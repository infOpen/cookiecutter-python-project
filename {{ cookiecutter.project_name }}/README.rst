{{ cookiecutter.project_name }}
============

{{ cookiecutter.project_description }}

Installation
------------

.. note:: You must use a dedicated virtualenv to install this project

- Install build dependencies and package

.. code:: bash

    pip install -r requirements.txt


.. note:: Need to be done after repository clone and git initialization,
          to enable project pre-commits

- Install pre-commits

.. code:: bash

    pre-commit install


Usage
-----

Run tests
~~~~~~~~~

.. code:: bash

    python setup.py test

Build documentation
~~~~~~~~~~~~~~~~~~~

.. code:: bash

    python setup.py doc

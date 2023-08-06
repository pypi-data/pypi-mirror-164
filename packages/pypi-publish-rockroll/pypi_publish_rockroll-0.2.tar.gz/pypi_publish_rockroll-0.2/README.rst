

Example Project
===============
This project provides an example to show how to publish python packages on PyPI.
You can refer to https://pypi.org/help/#publishing and also Giorgo's article https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3 for your reference.

Installing
============

.. code-block:: bash

    pip install example-publish-pypi-medium

Usage
=====

.. code-block:: bash

    >>> from src.example import custom_sklearn
    >>> custom_sklearn.get_sklearn_version()
    '0.24.2'

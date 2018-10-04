=====
waves
=====


.. image:: https://img.shields.io/pypi/v/pymt_waves.svg
        :target: https://pypi.python.org/pypi/pymt_waves

.. image:: https://img.shields.io/travis/mcflugen/pymt_waves.svg
        :target: https://travis-ci.org/mcflugen/pymt_waves

.. image:: https://readthedocs.org/projects/pymt_waves/badge/?version=latest
        :target: https://pymt_waves.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


PyMT plugin for Waves


* Free software: MIT license
* Documentation: https://waves.readthedocs.io.


---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

---------------------
Installing pymt_waves
---------------------

Once `pymt` is installed, the dependencies of `pymt_waves` can
be installed with:

.. code::

  conda install cem

To install `pymt_waves`,

.. code::

  conda install pymt_waves

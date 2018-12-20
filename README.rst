=====================
pytest-fixture-marker
=====================

.. image:: https://img.shields.io/pypi/v/pytest-fixture-marker.svg
    :target: https://pypi.org/project/pytest-fixture-marker
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-fixture-marker.svg
    :target: https://pypi.org/project/pytest-fixture-marker
    :alt: Python versions

.. image:: https://travis-ci.org/rciorba/pytest-fixture-marker.svg?branch=master
    :target: https://travis-ci.org/rciorba/pytest-fixture-marker
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/rciorba/pytest-fixture-marker?branch=master
    :target: https://ci.appveyor.com/project/rciorba/pytest-fixture-marker/branch/master
    :alt: See Build Status on AppVeyor

A pytest plugin to add markers based on fixtures used.

----

Why
---

Ever found yourself wanting to run all tests that use a certain fixture? This plugin will allow you
to do that.


Installation
------------
You can install "pytest-fixture-marker" via `pip`_ from `PyPI`_::

    $ pip install pytest-fixture-marker


Usage
-----
Once installed, the plugin will automatically mark each test. Marker names are generated from the
fixture names.::

    $ # run all tests that use the tempdir fixture
    $ pytest -m tempdir_fixture


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-fixture-marker" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/rciorba/pytest-fixture-marker/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project

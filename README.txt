Introduction
============

This package provides a buildout recipe based on `zc.recipe.testrunner`_ to
install a test script for `corejet.testrunner`_.

Usage
=====

In your buildout, add a part like this::

    [buildout]
    parts =
        ...
        test

    ...

    [test]
    recipe = corejet.recipe.testrunner
    eggs =
        my.package
    defaults = ['--auto-color', '--auto-progress']

The recipe accepts the same options as `zc.recipe.testrunner`_, so look at
its documentation for details.

When buildout is run, you should have a script in ``bin/test`` and a directory
``parts/test``.

To run the tests, use the ``bin/test`` script. If you pass the ``--xml``
option, test reports will be written to ``parts/test/testreports`` directory::

    $ bin/test --xml -s my.package

If you are using Hudson, you can now configure the build to publish JUnit
test reports for ``<buildoutdir>/parts/test/testreports/*.xml``.

To output a CoreJet report, do::

    $ bin/test --corejet="file,path/to/corejet/file.xml" -s my.package

The CoreJet report and output XML file will be placed in
``parts/test/corejet``. You can combine ``--xml`` and ``--corejet``.

The example above uses the ``file`` CoreJet repository source, which expects
to find a CoreJet XML file at the path specified after the comma.

.. _zope.testrunner: http://pypi.python.org/pypi/zope.testrunner
.. _zc.recipe.testrunner: http://pypi.python.org/pypi/zc.recipe.testrunner
.. _corejet.core: http://pypi.python.org/pypi/corejet.core
.. _corejet.testrunner: http://pypi.python.org/pypi/corejet.testrunner


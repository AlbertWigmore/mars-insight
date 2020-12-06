Release Guidelines
==================

The following steps are used as a guide to help with the making of a new release.

#. Create new branch.
#. Ensure that all tests passed using `nox`.
#. Update version number in `setup.py` and `mars-insight/__init__.py` following semantic versioning.
#. Add all
#. Push to GitHub and ensure CI passes.
#. PR
#. Merge and delete
#. Tag new version and make release
#. Push to PyPI
#. Push to read the docs
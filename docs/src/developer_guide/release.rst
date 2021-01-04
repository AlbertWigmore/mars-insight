Release Guidelines
==================

The following steps are used as a guide to help with the making of a new release.

1. Create new branch with version name.
2. Ensure that all tests passed using `nox`.
3. Update version number in `setup.py` and `mars-insight/__init__.py` following semantic versioning.
4. Add all new changes to the changelog and fix the date to now.
5. Push changes to GitHub and ensure bnoth the CI and docs build passes. If not then apply fixes until they are.
6. Once everything is passing create a PR to merge into master branch and wait for review and approval.
7. Merge branch and delete.
8. Create new release with relevant information.
9. Check release CI passes and wheels/docs succesfully uploaded.

Changelog
=========


0.1.6 (2022-03-04)
------------------

New Features:

- New generic crumb class .base.UidCrumb

Miscellaneous:

- Converted the .base module in a subpackage.

[tobiasherp]


0.1.5 (2022-01-18)
------------------

Bugfixes:

- From ``hub['getbrain']`` we expect a brain, of course, rather than an object

[tobiasherp]


0.1.4 (2020-12-16)
------------------

Bugfixes:

- Fixed a NameError in certain breadcrumbs

Improvements:

- Python 3 compatibility, using six_
- Sorted imports, using isort_

Requirements:

- six_

Miscellaneous:

- Removed the currently empty `test` extra

[tobiasherp]


0.1.3 (2020-07-02)
------------------

Miscellaneous:

- (For now) hard-coded media center support

[tobiasherp]


0.1.2 (2020-03-05)
------------------

- Provides "feature" ``VisaplanTentativeBreadcrumbs``
  The feature ``VisaplanBreadcrumbs`` will be provided by version 1+.

  You may provide an oldcrumbs module depending on VisaplanTentativeBreadcrumbs,
  and a crumbs module depending on VisaplanBreadcrumbs

[tobiasherp]


0.1.1 (2019-11-27)
------------------

- Reduced logging.

- Tools update
  [tobiasherp]


0.1 (2018-09-18)
----------------

- Initial release.
  [tobiasherp]

.. _isort: https://pypi.org/project/isort
.. _six: https://pypi.org/project/six

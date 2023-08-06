# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._data
"""

# Python compatibility:
from __future__ import absolute_import

# Setup tools:
import pkg_resources

# Zope:
import zope.component.hooks  # important side effects?

try:
    pkg_resources.get_distribution('visaplan.plone.unitracctool')
except pkg_resources.DistributionNotFound:
    HAS_VISAPLANPLONEUNITRACCTOOL = False
    MYUNITRACC_UID = TEMP_UID = ('something', 'completely', 'different')
else:
    HAS_VISAPLANPLONEUNITRACCTOOL = True
    # visaplan:
    from visaplan.plone.unitracctool.unitraccfeature.utils import (
        MYUNITRACC_UID,
        TEMP_UID,
        )


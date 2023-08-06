# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._info

The UidCrumb class is currently used to create @@info or @@courseinfo
breadcrumbs; they will like become obsolete, though, when the parents-based
crumbs take the @@landing_path into account.
"""

# Python compatibility:
from __future__ import absolute_import

# Local imports:
from ._base import BaseCrumb
from visaplan.plone.breadcrumbs.utils import crumbdict


class UidCrumb(BaseCrumb):
    """
    Generic crumb for pages which present another object using the uid
    (usually an immediate child)
    """
    def tweak(self, crumbs, hub, info):
        uid = info['uid']
        if uid is not None:
            brain = hub['getbrain'](uid)
            if brain is not None:
                tid = self.id
                copa = info['path']  # context path
                crumbs.append(crumbdict(
                    brain.Title,
                    '%(copa)s/@@%(tid)s?uid=%(uid)s' % locals()))

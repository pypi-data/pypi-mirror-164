# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._context
"""

# Python compatibility:
from __future__ import absolute_import

# Local imports:
from ._base import BaseCrumb
from visaplan.plone.breadcrumbs.utils import crumbdict


class ContextCrumb(BaseCrumb):
    """
    Das Label wird bei Instantiierung übergeben
    und bei Ausführung übersetzt
    """
    def __init__(self, id, label, parents):
        self.label = label
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        _ = hub['translate']
        crumbs.append(crumbdict(
            _(self.label),
            self.id))

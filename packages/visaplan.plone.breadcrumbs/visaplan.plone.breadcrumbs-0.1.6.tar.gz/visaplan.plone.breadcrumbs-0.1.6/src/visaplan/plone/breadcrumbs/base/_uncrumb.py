# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._uncrumb
"""

# Local imports:
from ._base import BaseCrumb
from ._exceptions import NoCrumbsException


# --------- [ spezielle Brotkrümel- (Nicht-Krümel-) Klassen ... [
class NoCrumbs(BaseCrumb):
    """
    Kurzschluß: Es liegt ein Request vor, für den *keinerlei*
    Breadcrumbs erzeugt werden sollen.
    """
    def tweak(self, crumbs, hub, info):
        raise NoCrumbsException(self.__class__.__name__, self.id)


class SkipCrumb(BaseCrumb):
    """
    Für dieses Template soll kein Krümel erzeugt werden
    (etwaige Parents werden aber ausgeführt).

    Siehe auch --> SkipCrumbException
    """
    def tweak(self, crumbs, hub, info):
        pass
# --------- ] ... spezielle Brotkrümel- (Nicht-Krümel-) Klassen ]

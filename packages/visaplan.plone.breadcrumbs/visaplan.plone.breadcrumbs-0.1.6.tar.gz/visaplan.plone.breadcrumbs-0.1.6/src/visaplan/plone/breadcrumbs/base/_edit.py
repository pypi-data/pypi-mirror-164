# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._base
"""
# TODO: unnötige Breadcrumb-Klassen eliminieren
#       (möglichst auf Grundtypen zurückführen)

# Python compatibility:
from __future__ import absolute_import

# Setup tools:
import pkg_resources

# Zope:
import zope.component.hooks

# visaplan:
from visaplan.plone.base.typestr import pt_string

# Local imports:
from ._base import BaseCrumb
from ._devel import tellabout_call
#
from ._log import logger
from visaplan.plone.breadcrumbs.utils import crumbdict


class BaseEditCrumb(BaseCrumb):
    """
    Bearbeiten: wenn neues Objekt, dann kein href-Attribut erzeugen

    Das Label ist der Titel des bearbeiteten Objekts; wird dies gerade erst
    erzeugt, hängt es vom Typ ab.
    """

    @tellabout_call #(2)
    def tweak(self, crumbs, hub, info):
        # set_trace()
        if info['context_title']:
            raw_title = 'Edit'
            url = self._context_url(info, self.id)
        else:
            try:
                raw_title = pt_string[info['portal_type']]['New thingy']
            except KeyError as e:
                pt = info['portal_type']
                context = info['context']
                logger.error('%(self)s: KeyError %(e)r (%(pt)r, %(context)r)',
                             locals())
                raw_title = 'Edit'
            url = None
        crumbs.append(crumbdict(
            hub['translate'](raw_title),
            url))

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
from visaplan.tools.dicts import subdict_forquery
from visaplan.tools.minifuncs import gimme_None

# Local imports:
from ._devel import tellabout_call
#
from ._exceptions import (
    BreadcrumbsException,
    NoCrumbsException,
    SkipCrumbException,
    )
from ._log import debug_active

# Logging / Debugging:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import pp


# -------------------- [ Brotkrümel-Basisklasse "BaseCrumb" ... [
class BaseCrumb:
    """
    Virtuelle Basisklasse für alle Brotkrümelklassen.
    Bei der Generierung der Brotkrümel für einen konkreten Request werden
    Instanzen dieser Klassen verwendet (Brotkrümelfunktionen), die zu Beginn
    (bei Import des Moduls) erzeugt werden.
    """

    def __init__(self, id, parents=[]):
        """
        id -- entspricht meist der ID des aufrufenden Seitentemplates
              und wird in vielen Brotkrümelklassen entsprechend für den
              erzeugten Krümel verwendet
        parents -- eine Sequenz von Brotkrümelfunktionen, zumeist mit einem
                   einzigen Element
        """
        self.id = id
        self.parents = list(parents)
        if debug_active >= 2:
            self.tell()

    # @tellabout_call
    def __call__(self, crumbs, hub, info):
        """
        Es wird kein Wert zurückgegeben; die Liste "crumbs" wird
        in-place geändert, ebenso wie hub und info.
        """
        # es ist eigentlich immer genau *ein* parent:
        for parent in self.parents:
            parent(crumbs, hub, info)
        self.tweak(crumbs, hub, info)
        if debug_active:
            pp('Breadcrumbs-Klasse: %r' % self.__class__,
               'info (Auszug):',
               subdict_forquery(info,
                                ['is_view_template',
                                 'view_url',
                                 'view_template_id',
                                 'view_template_done',
                                 ],
                                defaults_factory=gimme_None,
                                strict=False),
               'crumbs am Ende von __call__:',
               crumbs)

    def getParent(self):
        """
        Verwendet zum Bauen eines Strukturbaums.
        Bislang haben alle Instanzen maximal ein Elternelement,
        was für die Brotkrümelgenerierung ohne Bedeutung ist.
        Diese Methode erzwingt es jedoch.
        """
        if not self.parents:
            return None
        elif self.parents[1:]:
            raise ValueError('%s: Zu viele Eltern! (%s)'
                             % (self, self.parents))
        else:
            return self.parents[0]

    def tweak(self, crumbs, hub, info):
        """
        Diese Methode muß in abgeleiteten Klassen überschrieben werden;
        sie nimmt die spezifischen Änderungen vor.
        """
        raise NotImplementedError

    def __str__(self):
        if self.parents:
            return '%s[%r, parents: %s]' % (
                    self.__class__.__name__,
                    self.id,
                    self.parents,
                    )
        return '%s[%r]' % (
                self.__class__.__name__,
                self.id,
                )

    def __repr__(self):
        return '<%s(%r)>' % (self.__class__.__name__, self.id)

    def _brain_id_and_gid(self, brain, gid, tid=None):
        """
        Da sehr oft gebraucht ...
        """
        url = brain.getURL()
        if tid is None:
            tid = self.id
        return '%(url)s/%(tid)s?gid=%(gid)s' % locals()

    def _context_url(self, info, tid):
        """
        URL des Objekts aus dem Kontext
        """
        url = info['context_url']
        gid = info['gid']
        if gid is not None:
            return '%(url)s/%(tid)s?gid=%(gid)s' % locals()
        else:
            return '%(url)s/%(tid)s' % locals()

    def _desktop_subpage_url(self, info, tid=None):
        """
        URL einer Unterseite des Schreibtischs
        """
        if tid is None:
            tid = self.id
        url = info['desktop_url']
        gid = info['gid']
        if gid is not None:
            return '%(url)s/%(tid)s?gid=%(gid)s' % locals()
        else:
            return '%(url)s/%(tid)s' % locals()

    def _desktop_url(self, info):
        """
        URL des Schreibtischs
        """
        if info['gid'] is not None:
            return '%(desktop_url)s?gid=%(gid)s' % info
        else:
            return '%(desktop_url)s' % info

    def _rooted_url(self, info, tid):
        """
        URL einer direkten Unterseite des Portals
        """
        url = info['portal_url']
        return '%(url)s/%(tid)s' % locals()

    def tell(self, verbose=0):
        """
        Für Debugging: Selbstauskunft
        """
        args = ['%s(%r):' % (
                self.__class__.__name__,
                self.id,
                )]
        if verbose:
            args.append(('*** parents:', self.parents))
        else:
            args.append('%d parents' % len(self.parents))
        pp(*args)
# -------------------- ] ... Brotkrümel-Basisklasse "BaseCrumb" ]

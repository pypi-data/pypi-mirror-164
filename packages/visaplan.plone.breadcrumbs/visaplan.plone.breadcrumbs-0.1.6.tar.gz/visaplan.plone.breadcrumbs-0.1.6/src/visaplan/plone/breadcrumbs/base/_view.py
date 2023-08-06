# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._view
"""
# TODO: unnötige Breadcrumb-Klassen eliminieren
#       (möglichst auf Grundtypen zurückführen)

# Python compatibility:
from __future__ import absolute_import

# Local imports:
from ._base import BaseCrumb
from ._devel import tellabout_call
#
from ._log import debug_active, logger
from visaplan.plone.breadcrumbs.utils import crumbdict

# Logging / Debugging:
from visaplan.tools.debug import log_or_trace, pp


class GenericContainerCrumb(BaseCrumb):
    """
    Als Elternkrümel, z. B. für "view"
    """
    def tweak(self, crumbs, hub, info):
        if info['skip_desktop_crumbs']:
            return
        has_group = info['gid'] is not None
        try:
            tup = pt2tup[info['portal_type']][has_group]
        except KeyError as e:
            context = info['context']
            logger.error('%(self)s: kein Template für %(pt)r (%(context)r)',
                         locals())
        else:
            crumbs.append(crumbdict(
                hub['translate'](tup[0]),
                self._desktop_subpage_url(info, tup[1])))


# currently used in ...
# - visaplan.plone.groups.groupdesktop.crumbs
# - visaplan.plone.elearning.unitracccourse.crumbs
class ViewCrumb(BaseCrumb):
    """
    Spezifischer View-Krümel, z. B. für "unitraccnews_view";
    die Beschriftung wird dem Kontext entnommen.
    Es wird die übergebene id verwendet.

    Allgemeine View-Krümel werden aus der Struktur erzeugt,
    siehe --> _par_naive.py, BaseParentsCrumbs;
    diese Klasse erzeugt Krümel nur noch,
    wenn das verwendete Template nicht das Standard-Template des Objekts ist,
    oder wenn dieser Krümel durch den (Gruppen-) Schreibtisch gelöscht wurde.

    Der Titel ist entsprechend nicht mehr der Objekttitel (der ja schon in
    Verwendung sein sollte), sondern eine "Übersetzung" des Template-Titels.

    Siehe auch -> GenericViewCrumb; zusammenführen?
    """
    # @log_or_trace(debug_active, trace_key='viewcrumb', trace=0)
    def tweak(self, crumbs, hub, info):
        # info['view_url'], info['view_template_id'], info['is_view_template']
        # pp(self.__class__, info)
        if info['personal_desktop_done']:
            # Der Krümel wurde vom Schreibtisch gelöscht und nun hier neu
            # erzeugt:
            crumbs.append(crumbdict(
                info['context_title'],
                info['view_url']))
            info['view_template_done'] = True
            return
        elif info['is_view_template']:
            # Der Krümel für die Standardansicht (mit Objekttitel) wird von
            # BaseParentsCrumbs aus der Objektstruktur erzeugt ...
            return

        tid = self.id
        crumbs.append(crumbdict(
            hub['translate'](tid),
            self._context_url(info, tid)))
        return  # pep 20.2


class GenericViewCrumb(BaseCrumb):
    """
    Allgemeine View-Krümel werden aus der Struktur erzeugt,
    siehe --> BaseParentsCrumbs;  diese Klasse erzeugt Krümel nur noch,
    wenn das verwendete Template nicht das Standard-Template des Objekts ist,
    oder wenn dieser Krümel durch den (Gruppen-) Schreibtisch gelöscht wurde.

    Der Titel ist entsprechend nicht mehr der Objekttitel (der ja schon in
    Verwendung sein sollte), sondern eine "Übersetzung" des Template-Titels.

    Siehe auch -> ViewCrumb; zusammenführen?
    """
    @tellabout_call #(2)
    def tweak(self, crumbs, hub, info):
        is_new = not info['context_title']
        info['view_url'], info['view_template_id'], info['is_view_template']
        # pp(self.__class__, info)
        # XXX ??? Dokumentieren? (evtl. obsolet)
        is_published = len(crumbs) >= 3
        if not is_published:
            # generic_container_crumb(crumbs, hub, info)
            registered('--generic container--')(crumbs, hub, info)

        # wenn das Objekt noch keinen Titel hat, wird es gerade erst erzeugt
        # und kann noch nicht beguckt werden:
        if is_new:
            return
        if info['personal_desktop_done']:
            # Der Krümel wurde vom Schreibtisch gelöscht und nun hier neu
            # erzeugt:
            crumbs.append(crumbdict(
                info['context_title'],
                info['view_url']))
            info['view_template_done'] = True
            return
        elif info['is_view_template']:
            # Der Krümel für die Standardansicht (mit Objekttitel) wird von
            # BaseParentsCrumbs aus der Objektstruktur erzeugt ...
            return

        tid = self.id
        crumbs.append(crumbdict(
            hub['translate'](tid),
            self._context_url(info, tid)))

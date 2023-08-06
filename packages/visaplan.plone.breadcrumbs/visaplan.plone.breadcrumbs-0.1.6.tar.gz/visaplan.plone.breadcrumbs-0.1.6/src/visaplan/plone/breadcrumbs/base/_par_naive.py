# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._par_naive

This is our traditional functionality for parents-based breadcrumbs;
it is "naive" in not taking @@mainmenu information into account.

"""
# Python compatibility:
from __future__ import absolute_import

# visaplan:
from visaplan.plone.base.typestr import pt_string

# Local imports:
from ._base import BaseCrumb
from ._data import MYUNITRACC_UID, TEMP_UID
from ._log import debug_active, logger
from ._registry import registered
from visaplan.plone.breadcrumbs._vars import (
    LISTING_TEMPLATES,
    NODESKTOP_TEMPLATES,
    )
from visaplan.plone.breadcrumbs.utils import (
    LAST_NONFOLDERISH_BASECRUMB_KEY,
    crumbdict,
    title_or_caged_id__tup,
    )


class BaseParentsCrumbs(BaseCrumb):

    """
    Keine Registrierung, keine ID; wird IMMER zuerst ausgeführt.
    Erzeugt Krümel für alle akquirierten Container,
    incl. der virtuellen Container "persönlicher" und "Gruppenschreibtisch"
    (durch Aufruf der DesktopCrumbs-Instanz registered('group-desktop')).
    """

    # @log_or_trace(debug_active, trace_key='base_crumbs', trace=0)
    def tweak(self, crumbs, hub, info):
        list_ = list(hub['parents'])
        list_.reverse()
        lnf_idx = None
        desktop_found = False
        mediacenter_found = False
        tid = info['template_id']
        boring_template = tid not in LISTING_TEMPLATES

        for o in list_[1:]:  # Zope-Root ignorieren
            try:
                ouid = o.UID()
                o_id = o.getId()
                if o.portal_type == 'Plone Site':
                    crumbs.append(
                            crumbdict(hub['translate']('Home'),
                                      info['portal_url']))
                    continue
                elif o.getExcludeFromNav():
                    if o_id == 'mediathek':  # TODO: regard subportal settings
                        mediacenter_found = True
                        pt = info['portal_type']
                        _ = hub['translate']
                        try:
                            pt_dic = pt_string[pt]
                            thingies = _(pt_dic['thingies'])
                            mediacenter_path = '/media'  # TODO: regard @@sp s.
                            crumbs.extend([
                                crumbdict(_('Media center'),
                                          mediacenter_path),
                                crumbdict(_(pt_dic['Thingies']),
                                          mediacenter_path + '/' + thingies),
                                ])
                        except Exception as e:
                            context = info['context']
                            logger.error(
                                '%(self)s: %(e)r processing'
                                ' mediacenter breadcrumbs for %(context)r',
                                locals())
                            crumbs.append(crumbdict('ERROR', None))

                        break
                    elif boring_template:
                        if ouid == TEMP_UID:
                            desktop_found = True
                            break
                        else:
                            continue
                    # Listing-Template gefunden - normal fortfahren
            except AttributeError as e:
                continue
            else:
                # TODO: use subportal settings (pages['desktop'])
                if ouid == MYUNITRACC_UID:
                    registered('group-desktop')(crumbs, hub, info)
                    break
                # falls der temp-Ordner nicht von
                # der Navigation ausgeschlossen ist:
                elif ouid == TEMP_UID:
                    desktop_found = True
                    # hier liegen die unveröffentlichten Objekte,
                    # incl. derer auf dem persönlichen Schreibtisch
                    if boring_template:
                        break
                elif (ouid == TEMP_UID
                      and info['template_id'] not in NODESKTOP_TEMPLATES
                      ):
                    # Temp-Ordner --> Schreibtisch:
                    registered('group-desktop')(crumbs, hub, info)
                    break
                else:
                    title, do_translate = title_or_caged_id__tup(o)
                    if do_translate:
                        title = hub['translate'](title)
                    crumbs.append(
                            crumbdict(title,
                                      o.absolute_url()))
                    if o.isPrincipiaFolderish:
                        lnf_idx = None
                    else:
                        lnf_idx = len(crumbs) - 1
        # wenn temp-Ordner nicht im Pfad, keinen Schreibtisch erzeugen:
        if not info['skip_desktop_crumbs'] and not desktop_found:
            info['skip_desktop_crumbs'] = True

        info[LAST_NONFOLDERISH_BASECRUMB_KEY] = lnf_idx
        if not info['skip_desktop_crumbs']:
            registered('group-desktop')(crumbs, hub, info)

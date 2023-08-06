# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._base
"""

# Python compatibility:
from __future__ import absolute_import

from six.moves.urllib.parse import urlencode

# Local imports:
from ._base import BaseCrumb
from visaplan.plone.breadcrumbs.utils import (
    LAST_NONFOLDERISH_BASECRUMB_KEY,
    crumbdict,
    )


class RootedCrumb(BaseCrumb):
    """
    Generischer Krümel für in der Portalwurzel angesiedelte Seiten

    Das Label wird bei Instantiierung angegeben.
    """
    def __init__(self, id, label, parents=[]):
        """
        eingeschobenes Pflichtargument: die Beschriftung
        """
        self._raw_label = label
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._rooted_url(info, self.id)))


class DesktopBrowserCrumb(RootedCrumb):
    """
    Generischer Krümel für Unterseiten des Schreibtischs, die zusätzlich die
    Angabe eines Browsers benötigen.

    Das Label und der Browser werden bei Instantiierung angegeben.
    """
    def __init__(self, id, label, browser, parents=[]):
        """
        eingeschobene Pflichtargumente:
        - die Beschriftung (wie RootedCrumb)
        - der Browser
        """
        assert id is not None
        if browser is None:
            self._virtual_id = '@@%(id)s' % locals()
        elif browser:
            self._virtual_id = '@@%(browser)s/%(id)s' % locals()
        else:
            self._virtual_id = '@@%(id)s' % locals()
        RootedCrumb.__init__(self, id, label, parents)

    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._desktop_subpage_url(info, self._virtual_id)))


class RootedBrowserCrumb(DesktopBrowserCrumb):
    """
    Dieselbe Initialisierungslogik wie DesktopBrowserCrumb, aber nicht für den
    Schreibtisch, sondern relativ zur Portalwurzel.

    Mit leerem Browser z. B. '@@syndication-settings'

    Das Label und der Browser werden bei Instantiierung angegeben.

    Wenn das Präfix '@@' stört (bzw. nicht funktionieren würde), stattdessen
    einfach --> RootedCrumb verwenden!
    """
    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            hub['translate'](self._raw_label),
            self._rooted_url(info, self._virtual_id)))


class RootedUidCrumb(BaseCrumb):
    """
    Generischer Krümel für Seiten mit einer Request-Variablen 'uid'

    Das Label ist der Title des Objekts mit der angegebenen UID.
    """
    def tweak(self, crumbs, hub, info):
        uid = info['uid']
        if uid is not None:
            brain = hub['getbrain'](uid)
            if brain is not None:
                tid = self.id
                crumbs.append(crumbdict(
                    brain.Title,
                    '/%(tid)s?uid=%(uid)s' % locals()))


class RootedRequestvarCrumb(BaseCrumb):
    """
    Das Label wird einer Request-Variablen entnommen.

    Siehe auch --> RootedUidCrumb.
    """
    def __init__(self, id, key, parents=[]):
        """
        key -- der Name der Request-Variablen
        """
        self._key = key
        BaseCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        key = self._key
        val = info['request_var'].get(key)
        if val:
            query_s = urlencode([(key, val)])
            crumbs.append(crumbdict(
                val,
                self._rooted_url(info, '?'.join((self.id, query_s)))))
        elif val is not None:
            info['request_var'][key] = None


class RootedCrumbWithChild(RootedCrumb, RootedRequestvarCrumb):
    """
    Ein fixer Krümel, und einer, der von einer Request-Variablen abhängt;
    der Wert dieser Variablen ist das Label des variablen Krümels
    """
    def __init__(self, id, label, key, parents=[]):
        """
        eingeschobenes Pflichtargument: die Beschriftung
        """
        self._key = key
        RootedCrumb.__init__(self, id, label, parents)

    def tweak(self, crumbs, hub, info):
        RootedCrumb.tweak(self, crumbs, hub, info)
        RootedRequestvarCrumb.tweak(self, crumbs, hub, info)


class RootedInfokeyCrumb(RootedRequestvarCrumb):
    """
    Das Label wird einem Schlüssel des info-Dictionarys entnommen.
    Die URL wird von einer übergebenen Funktion erzeugt.
    """
    # XXX: am 28.1.2015 keine weiteren Vorkommen gefunden
    def __init__(self, id, key, urlfunc, parents=[]):
        """
        key -- der Name der Request-Variablen (aus RootedRequestvarCrumb)
        urlfunc -- Funktion, um die URL zu erzeugen
        """
        self._urlfunc = urlfunc
        RootedRequestvarCrumb.__init__(self, id, key, parents)

    def tweak(self, crumbs, hub, info):
        key = self._key
        val = info[key]
        if val:
            func = self._urlfunc
            crumbs.append(crumbdict(
                val,
                func(crumbs, hub, info)))


class RootedDefaultCrumb(BaseCrumb):
    """
    Generischer Krümel für vergessene Managementseiten.
    Nicht schön, aber vorhanden, und etwaige parents werden verarbeitet
    (i.e. insbesondere die Management-Zentrale).
    """
    def tweak(self, crumbs, hub, info):
        crumbs.append(crumbdict(
            self.id,  # nicht schön genug? Was schöneres explizit registrieren!
            self._rooted_url(info, self.id)))

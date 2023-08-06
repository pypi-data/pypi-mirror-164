# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
base-Modul für visaplan.plone.breadcrumbs

Instantiierbare Klassen, Exception-Klassen;
register, registered
"""
# TODO: unnötige Breadcrumb-Klassen eliminieren
#       (möglichst auf Grundtypen zurückführen)

# Python compatibility:
from __future__ import absolute_import, print_function

from six.moves import map

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           4,  # converted to subpackage
           0,  # Verwendung von print_indented entfernt
           )
__version__ = '.'.join(map(str, VERSION))

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

# Local imports:
from ._base import BaseCrumb
from ._context import ContextCrumb
from ._devel import tellabout_call
from ._edit import BaseEditCrumb
from ._exceptions import (
    BreadcrumbsException,
    NoCrumbsException,
    SkipCrumbException,
    )
from ._info import UidCrumb
from ._log import debug_active, logger
from ._par_naive import BaseParentsCrumbs
from ._registry import register, registered
from ._rooted import (
    DesktopBrowserCrumb,
    RootedBrowserCrumb,
    RootedCrumb,
    RootedCrumbWithChild,
    RootedDefaultCrumb,
    RootedInfokeyCrumb,
    RootedRequestvarCrumb,
    RootedUidCrumb,
    )
from ._uncrumb import NoCrumbs, SkipCrumb
from ._view import GenericContainerCrumb, GenericViewCrumb, ViewCrumb

__all__ = (
    # Brotkrümel-Basis:
    'BaseCrumb',              # _base.py
    # Vielseitig verwendbare Krümel:
    'RootedCrumb',            # _rooted.py
    'ContextCrumb',           # _context.py
    # Exception-Klassen:
    'BreadcrumbsException',   # _exceptions.py
    'NoCrumbsException',      # _exceptions.py
    'SkipCrumbException',     # _exceptions.py

    'BaseParentsCrumbs',      # _par_naive.py
    'UidCrumb',               # _info.py
    'RootedUidCrumb',         # _rooted.py
    'DesktopBrowserCrumb',    # _rooted.py
    'RootedBrowserCrumb',     # _rooted.py
    'RootedRequestvarCrumb',  # _rooted.py
    'RootedCrumbWithChild',   # _rooted.py
    'RootedInfokeyCrumb',     # _rooted.py
    # für dynamische Registrierung:
    'RootedDefaultCrumb',     # _rooted.py
    'GenericContainerCrumb',  # _view.py
    'ViewCrumb',              # _view.py
    'GenericViewCrumb',       # _view.py
    'BaseEditCrumb',          # _edit.py
    'NoCrumbs',               # _uncrumb.py
    'SkipCrumb',              # _uncrumb.py

    # Registry:
    'register',               # _registry.py
    'registered',             # _registry.py
    # Entwickungsunterstützung:
    'tellabout_call',         # _devel.py
    )

# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._registry
"""

# Python compatibility:
from __future__ import absolute_import

# Local imports:
from ._log import debug_active, logger

# Logging / Debugging:
from visaplan.tools.debug import pp


def make_registry():
    """
    Return a 3-tuple (set, get, show)
    """
    REGISTRY = {}
    def set(handler, id=None):
        if id is None:
            id = handler.id
        if id in REGISTRY:
            old_handler = REGISTRY[id]
            logger.warning('There is an existing crumb adapter with id %(id)r'
                           ' (%(old_handler)r; replaced by'
                           ' %(handler)r)',
                           locals())
        if id is not None:
            REGISTRY[id] = handler
        return handler

    def get(id):
        try:
            return REGISTRY[id]
        except KeyError:
            logger.error('registry: no breadcrumb handler %(id)r found',
                    locals())
            raise

    def show(doit=debug_active):
        if doit:
            pp(REGISTRY)

    return set, get, show


register, registered, show_registry = make_registry()

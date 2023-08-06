# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._devel
"""

# Python compatibility:
from __future__ import absolute_import, print_function

# Logging / Debugging:
from visaplan.tools.debug import pp


# --------- [ Brotkrümel-Registry: Entwickungsunterstützung ... [
def tellabout_call(f, tail=0):
    # chunks = [f.__class__.__name__]
    chunks = []
    if f.__name__ != '__call__':
        chunks.extend(('.', f.__name__))
    if 0:
        # print dir(f)
        args = ((f.__class__, f.__class__.__name__), (f, chunks))
        kwargs = dict([(key, getattr(f, key))
                       for key in dir(f)
                       if key.startswith('func')
                          and key != 'func_globals'
                       ])
        pp(*args, **kwargs)
    nesting_string = '  '
    mask_before = '<<< %(self)s%(funcname)s(%(context)s) ... <<<'
    mask_after = '>>> ... %(self)s%(funcname)s(%(context)s) >>>'

    def inner(self, crumbs, hub, info, *args, **kwargs):
        funcname = ''.join(chunks)
        if not info['_context_printed']:
            context = repr(info['context'])
            info['_context_printed'] = True
            # print self, self.__class__, self.__class__.__name__
        else:
            context = '...'
        print(mask_before % locals())
        res = f(self, crumbs, hub, info, *args, **kwargs)
        if tail:
            pp('Letzte %d Breadcrumbs:' % tail, crumbs[-tail:])
        print(mask_after % locals())
        return res
    return inner
# --------- ] ... Brotkrümel-Registry: Entwickungsunterstützung ]

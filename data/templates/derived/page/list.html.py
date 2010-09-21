from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1284951816.618762
_template_filename='/home/remix/dev/ChezWam/chezwam/templates/derived/page/list.html'
_template_uri='/derived/page/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<ul id="titles">\n')
        # SOURCE LINE 8
        for page in c.pages:
            # SOURCE LINE 9
            __M_writer(u'<li>\n    ')
            # SOURCE LINE 10
            __M_writer(escape(page.title))
            __M_writer(u' [')
            __M_writer(escape(h.link_to('visit', h.url_for('path', id=page.id))))
            __M_writer(u']\n</li>\n')
        # SOURCE LINE 13
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <h1 class="main">Page List</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



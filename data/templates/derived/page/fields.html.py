from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1284951715.7685111
_template_filename='/home/remix/dev/ChezWam/chezwam/templates/derived/page/fields.html'
_template_uri='/derived/page/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace('fields', context._clean_inheritance_tokens(), templateuri='/derived/nav/fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'fields')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        fields = _mako_get_namespace(context, 'fields')
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(escape(fields.body()))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Heading",
    h.text(name='heading'),
    required=False,
)))
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
    "Title",
    h.text(name='title'),
    required=True,
    field_desc = "Used as the heading too if you didn't specify one above"
)))
        # SOURCE LINE 16
        __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(escape(h.field(
    "Content",
    h.textarea(name='content', rows=7, cols=40),
    required=True,
    field_desc = 'The text that will make up the body of the page'
)))
        # SOURCE LINE 22
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1284951723.0485229
_template_filename='/home/remix/dev/ChezWam/chezwam/templates/derived/tag/list.html'
_template_uri='/derived/tag/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['buildrow', 'heading']


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
        def buildrow(tag,odd=True):
            return render_buildrow(context.locals_(__M_locals),tag,odd)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 21
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        if len(c.paginator):
            # SOURCE LINE 24
            __M_writer(u'<p>')
            __M_writer(escape( c.paginator.pager('$link_first $link_previous $first_item to $last_item of $item_count $link_next $link_last') ))
            __M_writer(u'</p>\n<table class="paginator"><tr><th>Tag ID</th><th>Tag Name</th></tr>\n')
            # SOURCE LINE 26
            counter=0 
            
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin()]))
            __M_writer(u'\n')
            # SOURCE LINE 27
            for item in c.paginator:
                # SOURCE LINE 28
                __M_writer(u'    ')
                __M_writer(escape(buildrow(item, counter%2)))
                __M_writer(u'\n    ')
                # SOURCE LINE 29
                counter += 1 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n')
            # SOURCE LINE 31
            __M_writer(u'</table>\n<p>')
            # SOURCE LINE 32
            __M_writer(escape( c.paginator.pager('~2~') ))
            __M_writer(u'</p>\n')
            # SOURCE LINE 33
        else:
            # SOURCE LINE 34
            __M_writer(u'<p>\n    No tags have yet been created.\n    <a href="')
            # SOURCE LINE 36
            __M_writer(escape(h.url_for(controller='tag', action='new')))
            __M_writer(u'">Add one</a>.\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buildrow(context,tag,odd=True):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <tr class="')
        # SOURCE LINE 6
        __M_writer(escape(odd and 'odd' or 'even'))
        __M_writer(u'">\n        <td valign="top">\n            ')
        # SOURCE LINE 8
        __M_writer(escape(h.link_to(
                tag.id,
                h.url_for(
                    controller=u'tag',
                    action='view',
                    id=unicode(tag.id)
                )
            )))
        # SOURCE LINE 15
        __M_writer(u'\n        </td>\n        <td valign="top">\n            ')
        # SOURCE LINE 18
        __M_writer(escape(tag.name))
        __M_writer(u'\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'<h1>Tag List</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()



from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1285180698.8219659
_template_filename='/home/remix/dev/chezwam/ChezWam/chezwam/templates/derived/page/view.html'
_template_uri='/derived/page/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'tags', 'heading', 'title']


# SOURCE LINE 19

from formencode import htmlfill
from webhelpers.html import literal


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
        capture = context.get('capture', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(escape(literal(c.page.content)))
        __M_writer(u'\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        if c.available_tags:
            # SOURCE LINE 25
            __M_writer(escape(literal(htmlfill.render(capture(self.tags, c.available_tags), c.selected_tags))))
            __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'<p>\n  <a href="')
        # SOURCE LINE 31
        __M_writer(escape(h.url_for(controller='page', action='list')))
        __M_writer(u'">All Pages</a>\n| <a href="')
        # SOURCE LINE 32
        __M_writer(escape(h.url_for(controller='page', action='new', section=c.page.section, before=c.page.before)))
        __M_writer(u'">New Page</a>\n| <a href="')
        # SOURCE LINE 33
        __M_writer(escape(h.url_for(controller='page', action='edit', id=c.page.id)))
        __M_writer(u'">Edit Page</a>\n| <a href="')
        # SOURCE LINE 34
        __M_writer(escape(h.url_for(controller='page', action='delete', id=c.page.id)))
        __M_writer(u'">Delete Page</a>\n</p>\n')
        # SOURCE LINE 37
        __M_writer(u'<p>\n  <a href="')
        # SOURCE LINE 38
        __M_writer(escape(h.url_for(pageid=c.page.id, controller='comment', action='list', id=None)))
        __M_writer(u'">Comments (')
        __M_writer(escape(str(c.comment_count)))
        __M_writer(u')</a>\n| <a href="')
        # SOURCE LINE 39
        __M_writer(escape(h.url_for(pageid=c.page.id, controller='comment', action='new', id=None)))
        __M_writer(u'">Add Comment</a>\n</p>\n')
        # SOURCE LINE 42
        __M_writer(u'<p>\n  <a href="')
        # SOURCE LINE 43
        __M_writer(escape(h.url_for(controller='section', action='new', section=c.page.section, before=c.page.before)))
        __M_writer(u'">New Section</a>\n| <a href="')
        # SOURCE LINE 44
        __M_writer(escape(h.url_for(controller='section', action='edit', id=c.page.section)))
        __M_writer(u'">Edit Section</a>\n| <a href="')
        # SOURCE LINE 45
        __M_writer(escape(h.url_for(controller='section', action='delete', id=c.page.section)))
        __M_writer(u'">Delete Section and Index Page</a>\n</p>\n')
        # SOURCE LINE 48
        __M_writer(u'<p><a href="')
        __M_writer(escape(h.url_for(controller='tag', action='list')))
        __M_writer(u'">All Tags</a>\n| <a href="')
        # SOURCE LINE 49
        __M_writer(escape(h.url_for(controller='tag', action='new')))
        __M_writer(u'">Add Tag</a></p>\n')
        # SOURCE LINE 51
        __M_writer(escape(parent.footer()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tags(context,available_tags):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n    <h2>Tags</h2>\n    ')
        # SOURCE LINE 10
        __M_writer(escape(h.form_start(h.url_for(controller='page', action='update_tags', id=c.page.id), method='post')))
        __M_writer(u'\n        ')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
            "Tags",
            h.checkbox_group('tags', selected_values=None, align="table", options=available_tags)
        )))
        # SOURCE LINE 14
        __M_writer(u'\n        ')
        # SOURCE LINE 15
        __M_writer(escape(h.field(field=h.submit(value="Save Tags", name='submit'))))
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>')
        __M_writer(escape(c.page.heading or c.page.title))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(c.page.title))
        return ''
    finally:
        context.caller_stack._pop_frame()



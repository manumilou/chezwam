from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1285200282.058512
_template_filename='/home/remix/dev/chezwam/ChezWam/chezwam/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'footer', 'flash', 'header', 'title', 'heading']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n\t<meta http-equiv="content-script-type" content="text/javascript">\n    <title>')
        # SOURCE LINE 9
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n\t<link href="/css/photostream.css" media="screen" rel="stylesheet" type="text/css" />\n\t<script type="text/javascript" src="/js/jquery-1.4.2.min.js"></script>\n    ')
        # SOURCE LINE 12
        __M_writer(escape(self.head()))
        __M_writer(u'\n</head>\n<body>\n<div id="container">\n<div id="header-region">\n    ')
        # SOURCE LINE 17
        __M_writer(escape(self.header()))
        __M_writer(u'\n')
        # SOURCE LINE 20
        __M_writer(u'</div>\n<div id="main">\n    ')
        # SOURCE LINE 22
        __M_writer(escape(self.heading()))
        __M_writer(u'\n\t')
        # SOURCE LINE 23
        __M_writer(escape(self.flash()))
        __M_writer(u'\n    ')
        # SOURCE LINE 24
        __M_writer(escape(next.body()))
        __M_writer(u'\n</div>\n    ')
        # SOURCE LINE 26
        __M_writer(escape(self.footer()))
        __M_writer(u'\n\n</div>\n</body>\n</html>\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 57
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n\t')
        # SOURCE LINE 34
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/main.css'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n<div id="footer">\n\t<p><a href="#top">Top ^</a></p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 60
        if session.has_key('flash'):
            # SOURCE LINE 61
            __M_writer(u'    <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\n    ')
            # SOURCE LINE 62

            del session['flash']
            session.save()
                
            
            # SOURCE LINE 65
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n<div id="header">\n\t<div class="inside">\n\t<a name="top"></a>\n\t<div class="home">\n\t\t<a href="')
        # SOURCE LINE 42
        __M_writer(escape(h.url_for('path', id=6)))
        __M_writer(u'"><img src="/images/home-normal.png" title="Chez Wam" alt="Chez Wam"/></a>\n\t</div>\n\t<div class="signature"><span>@</span>manumilou</div>\n\t</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'Chez Wam')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'<h1>')
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()



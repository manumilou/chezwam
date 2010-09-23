import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chezwam.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PhotostreamController(BaseController):

    def view(self):
        return render('/derived/photostream/view.html');

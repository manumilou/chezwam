import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chezwam.lib.base import BaseController, render
from chezwam import model
from chezwam.model import meta

log = logging.getLogger(__name__)

import formencode

class ValidBefore(formencode.FancyValidator):
    """Checks the ID specified in the before field is valid"""
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        # Check the value for before is in the section
        if values.get('before'):
            valid_ids = [nav.id for nav in nav_q.filter_by(
                section=values['section']).all()]
            if int(values['before']) not in valid_ids:
                raise formencode.Invalid("Please check the section "
                    "and before values", values, state)
        return values

class NewNavForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    path = formencode.validators.Regex(not_empty=True, regex='^[a-zA-Z0-9_-]+$')
    section = formencode.validators.Int(not_empty=True)
    before = formencode.validators.Int()
    chained_validators = [ValidBefore()]



class NavController(BaseController):

    def nopage(self, section, path):
		return render('/derived/nav/create_page.html')

    def nosection(self, section, path):
		return render('/derived/nav/create_section.html')
  

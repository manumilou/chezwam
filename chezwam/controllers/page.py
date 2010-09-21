import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import formencode
from formencode import htmlfill
from pylons import session
from sqlalchemy import delete

from chezwam.lib.base import BaseController, render
from chezwam import model
import chezwam.model.meta as meta
import chezwam.lib.helpers as h

log = logging.getLogger(__name__)

from chezwam.controllers.nav import NewNavForm, ValidBefore

class UniquePagePath(formencode.validators.FancyValidator):
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        query = nav_q.filter_by(section=values['section'],
            type='page', path=values['path'])
        if request.urlvars['action'] == 'save':
            # Ignore the existing id when performing the check
            query = query.filter(model.Nav.id != int(request.urlvars['id']))
        existing = query.first()
        if existing is not None:
            raise formencode.Invalid("There is already a page in this "
                "section with this path", values, state)
        return values

class NewPageForm(NewNavForm):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page. '
        }
    )
    heading = formencode.validators.String()
    title = formencode.validators.String(not_empty=True)
    chained_validators = [ValidBefore(), UniquePagePath()]

class ValidTags(formencode.FancyValidator):
    def _to_python(self, values, state):
        # Because this is a chained validator, values will contain
        # a dictionary with a tags key associated with a list of
        # integer values representing the selected tags.
        all_tag_ids = [tag.id for tag in meta.Session.query(model.Tag)]
        for tag_id in values['tags']:
            if tag_id not in all_tag_ids:
                raise formencode.Invalid(
                    "One or more selected tags could not be found in the database",
                    values,
                    state
                )
        return values

class ValidTagsForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    tags = formencode.foreach.ForEach(formencode.validators.Int())
    chained_validators = [ValidTags()]

class PageController(BaseController):

    def __before__(self):
		nav_q = meta.Session.query(model.Nav)
		c.available_sections = [(nav.id, nav.name) for nav in nav_q.filter_by(type='section')]

    def view(self, id=None):
		if id is None:
			abort(404)
		page_q = model.meta.Session.query(model.Page)
		c.page = page_q.get(int(id))
		if c.page is None:
			abort(404)
		c.comment_count =  meta.Session.query(model.Comment).filter_by(pageid=id).count()
		tag_q = meta.Session.query(model.Tag)
		c.available_tags = [(tag.id, tag.name) for tag in tag_q]
		c.selected_tags = {'tags':[str(tag.id) for tag in c.page.tags]}
		c.menu = request.environ['chezwam.navigation']['menu']
		c.tabs = request.environ['chezwam.navigation']['tabs']
		c.breadcrumbs = request.environ['chezwam.navigation']['breadcrumbs']
		return render('/derived/page/view.html')

    def new(self):
		return render('/derived/page/new.html')

    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
    	# Add the new page to the database
    	page = model.Page()
    	for k, v in self.form_result.items():
        	setattr(page, k, v)
    	meta.Session.add(page)
    	model.Nav.add_navigation_node(page, self.form_result['section'],
        	self.form_result['before'])
    	meta.Session.commit()
       	# Issue an HTTP redirect
		return redirect_to('path', id=page.id)

    def edit(self, id=None):
		if id is None:
			abort(404)
		page_q = meta.Session.query(model.Page)
		page = page_q.filter_by(id=id).first()
		if page is None:
			abort(404)
		values = {
			'name': page.name,
    		'path': page.path,
    		'section': page.section,
    		'before': page.before,
    		'title': page.title,
    		'heading': page.heading,
    		'content': page.content,
   	 	}
		c.title = page.title
		return htmlfill.render(render('/derived/page/edit.html'), values)
		
    @restrict('POST')
    @validate(schema=NewPageForm(), form='edit')
    def save(self, id=None):
    	page_q = meta.Session.query(model.Page)
    	page = page_q.filter_by(id=id).first()
    	if page is None:
        	abort(404)
		if not(page.section == self.form_result['section'] and \
			page.before == self.form_result['before']):
			model.Nav.remove_navigation_node(page)
			model.Nav.add_navigation_node(page, self.form_result['section'],
            	self.form_result['before'])
    	for k,v in self.form_result.items():
        	if getattr(page, k) != v:
				setattr(page, k, v)
    	meta.Session.commit()
		# Flash message and session
    	session['flash'] = 'Page successfully updated.'
    	session.save()
    	# Issue an HTTP redirect
    	response.status_int = 302
    	response.headers['location'] = h.url_for('path',
        	id=page.id)
    	return "Moved temporarily"

    def list(self):
		c.pages=meta.Session.query(model.Page).all()
		return render('/derived/page/list.html')

    def delete(self, id=None):
		if id is None:
			abort(404)
		page_q = meta.Session.query(model.Page)
		page = page_q.filter_by(id=id).first()
		if page is None:
			abort(404)
		meta.Session.execute(delete(model.pagetag_table, model.pagetag_table.c.pageid==page.id))
		model.Nav.remove_navigation_node(page)
		meta.Session.delete(page)
		meta.Session.commit()
		return render('/derived/page/deleted.html')	

    @restrict('POST')
    @validate(schema=ValidTagsForm(), form='view')
    def update_tags(self, id=None):
    	if id is None:
        	abort(404)
    	page_q = meta.Session.query(model.Page)
    	page = page_q.filter_by(id=id).first()
    	if page is None:
        	abort(404)
    	tags_to_add = []
    	for i, tag in enumerate(page.tags):
        	if tag.id not in self.form_result['tags']:
				del page.tags[i]
    	tagids = [tag.id for tag in page.tags]
    	for tag in self.form_result['tags']:
        	if tag not in tagids:
				t = meta.Session.query(model.Tag).get(tag)
            	page.tags.append(t)
    	meta.Session.commit()
    	session['flash'] = 'Tags successfully updated.'
    	session.save()
		# Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for('path',
            id=page.id)
        return "Moved temporarily"



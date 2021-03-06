"""Setup the ChezWam application"""
import logging

from chezwam.config.environment import load_environment
from chezwam.model import meta
from chezwam import model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup chezwam here"""
    load_environment(conf.global_conf, conf.local_conf)

	# Load the models
    meta.metadata.bind = meta.engine
    #filename = os.path.split(conf.filename)[-1]
    #if filename == 'test.ini':
     #   # Permanently drop any existing tables
      #  log.info("Dropping existing tables...")
      #  meta.metadata.drop_all(checkfirst=True)

    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)

    log.info("Adding home page...")
    section_home = model.Section()
    section_home.path=u''
    section_home.name=u'Home Section'
    meta.Session.add(section_home)
    meta.Session.flush()

    page_contact = model.Page()
    page_contact.title=u'Contact Us'
    page_contact.path=u'contact'
    page_contact.name=u'Contact Us Page'
    page_contact.content = u'Contact us page'
    page_contact.section=section_home.id
    meta.Session.add(page_contact)
    meta.Session.flush()

    section_dev = model.Section()
    section_dev.path=u'dev'
    section_dev.name=u'Development Section'
    section_dev.section=section_home.id
    section_dev.before=page_contact.id
    meta.Session.add(section_dev)
    meta.Session.flush()

    page_svn = model.Page()
    page_svn.title=u'SVN Page'
    page_svn.path=u'svn'
    page_svn.name=u'SVN Page'
    page_svn.content = u'This is the SVN page.'
    page_svn.section=section_dev.id
    meta.Session.add(page_svn)
    meta.Session.flush()

    page_dev = model.Page()
    page_dev.title=u'Development Home'
    page_dev.path=u'index'
    page_dev.name=u'Development Page'
    page_dev.content=u'This is the development home page.'
    page_dev.section=section_dev.id
    page_dev.before=page_svn.id
    meta.Session.add(page_dev)
    meta.Session.flush()

    page_home = model.Page()
    page_home.title=u'Home'
    page_home.path=u'index'
    page_home.name=u'Home'
    page_home.content=u'Welcome to the SimpleSite home page.'
    page_home.section=section_home.id
    page_home.before=section_dev.id
    meta.Session.add(page_home)
    meta.Session.flush()

    meta.Session.commit()
    log.info("Successfully set up.")

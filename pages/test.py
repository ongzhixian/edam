################################################################################
# Modules and functions import statements
################################################################################

import pdb
from helpers.app_helpers import *
from helpers.page_helpers import *
from helpers.jinja2_helpers import *

################################################################################
# Setup helper functions
################################################################################

# N/A

################################################################################
# Setup commonly used routes
################################################################################

@route('/test', method=['POST','GET'])
def display_home_page(errorMessages=None):
    context = get_default_context(request)
    if request.method == 'POST':
        logging.info("In test - POST")
    #logging.info("In test - GET")
    return jinja2_env.get_template('html/test/home-page.html').render(context)

@route('/test/register', method=['POST','GET'])
def display_register_page(errorMessages=None):
    context = get_default_context(request)
    if request.method == 'POST':
        pass
    return jinja2_env.get_template('html/test/register-page.html').render(context)

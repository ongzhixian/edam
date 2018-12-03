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

# RAM
# Resource Administration Module

@route('/ram')
@require_authentication
def display_home_page(errorMessages=None):
    context = get_default_context(request)
    #response.set_cookie('username', 'the username')
    return jinja2_env.get_template('html/ram/home-page.html').render(context)

@route('/ram/register', method=['POST','GET'])
@require_authentication
def display_register_page(errorMessages=None):
    context = get_default_context(request)
    if request.method == 'POST':
        pass
    
    return jinja2_env.get_template('html/ram/register-page.html').render(context)



# @route('/about')
# def display_about_page(errorMessages=None):
#     context = get_default_context(request)
#     return jinja2_env.get_template('html/site/about-page.html').render(context)

# @route('/contact')
# def display_contact_page(errorMessages=None):
#     context = get_default_context(request)
#     return jinja2_env.get_template('html/site/contact-page.html').render(context)

# @route('/services')
# def display_services_page(errorMessages=None):
#     context = get_default_context(request)
#     return jinja2_env.get_template('html/site/services-page.html').render(context)

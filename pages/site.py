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

@route('/favicon.ico')
def get_favicon():
    return bottle.static_file('favicon.ico', root='./')

@route('/<filename:path>')  
def static(filename):  
    '''  
    Serve static files
    '''  
    return bottle.static_file(filename, root='./static')

@route('/')
def display_home_page(errorMessages=None):
    context = get_default_context(request)
    #response.set_cookie('username', 'the username')
    return jinja2_env.get_template('html/site/home-page.html').render(context)

########################################
# Auth pages
########################################



# @route('/login', methods=['POST'])
# def display_login_page_post(errorMessages=None):
#     '''  
#     Login processing page
#     '''
#     logging.debug("IN display_login_page_post()")
#     context = get_default_context(request)
#     form_username = request.form['form_username']
#     form_password = request.form['form_password']
#     #     print(form_username)
#     #     logging.debug(form_password)
#     #     (is_valid_user, user) = ApplicationUser.is_valid_user(form_username, form_password)
#     #     logging.debug(is_valid_user)
#     # if is valid login page, set cookie and log user in
#     is_valid_user = True
#     if is_valid_user:
#         logging.debug("is_valid_user")
#         #cookie_body = make_cookie_body(user.username, ",".join(user.roles))
#         #context['auth_id'] = cookie_body
#         #resp = make_response(jinja2_env.get_template('html/site/home-page.html').render(context))
#         #resp.set_cookie(appconfig["application"]["auth_cookie_name"], cookie_body)
#         return jinja2_env.get_template('html/site/login-page.html').render(context)
#     else:
#         # else show invalid password
#         logging.debug("invalid password")
#         context['user_messages'] = [
#             { 'category': "ERROR", 'text' : "Invalid user credentials."}
#         ]
#         resp = jinja2_env.get_template('html/site/login-page.html').render(context)
#     return resp



########################################
# Other common site pages
########################################

@route('/about')
def display_about_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/about-page.html').render(context)

@route('/contact')
def display_contact_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/contact-page.html').render(context)

@route('/services')
def display_services_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/services-page.html').render(context)

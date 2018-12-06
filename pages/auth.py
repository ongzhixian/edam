################################################################################
# Modules and functions import statements
################################################################################

import logging
import pdb
import urllib
from helpers.app_helpers import *
from helpers.page_helpers import *
from helpers.jinja2_helpers import *

################################################################################
# Constants
################################################################################

#SQLITE_FILENAME = appconfig["url_dump"]["sqlite3_filename"]
AUTH_COOKIE_NAME = str(appconfig['application']["auth_cookie_name"])

################################################################################
# Setup helper functions
################################################################################

# N/A
def isValidCredential(username, password):
    if username == "zhixian" and password=="zhixian":
        return True
    return False

################################################################################
# Setup commonly used routes
################################################################################

# @route('/login')
# def display_login_page(errorMessages=None):
#     '''  
#     Login page
#     '''
#     logging.debug("IN display_login_page()")
#     context = get_default_context(request)
#     return jinja2_env.get_template('html/site/login-page.html').render(context)


@route('/login', method=['POST','GET'])
def display_login_page(errorMessages=None):
    context = get_default_context(request)
    if request.method == 'POST':
        username = request.forms['username_field'].strip()
        password = request.forms['password_field'].strip()
        # logging.debug("posting values")
        # for field_name in request.forms.keys():
        #     logging.debug(field_name)
        # logging.debug(username)
        # logging.debug(password)

        if isValidCredential(username, password):
            # do handling of POST here
            if AUTH_COOKIE_NAME not in request.cookies:
                cookie_value = add_auth_cookie(AUTH_COOKIE_NAME)
            else:
                cookie_value = request.cookies[AUTH_COOKIE_NAME]
            context['ERROR_MESSAGE'] = "AUTH OK"
            # logging.debug(str(dir(request)))
            # logging.debug(request.params)
            # for x in request.params:
            #     logging.debug(x)
            # pass
            logging.info("AFTER AUTH OK")
            if "from" in request.params:
                logging.info("in from")
                from_url = urllib.unquote(request.params["from"])
                logging.info("from_url is:[{0}]".format(from_url))
                #logging.debug("from_url is {0}".format(from_url))
                redirect(from_url)
        else:
            # Display a message that authentication failed.
            context['ERROR_MESSAGE'] = "AUTH FAILED"
            pass
    return jinja2_env.get_template('html/auth/login-page.html').render(context)


@route('/logout')
def display_logout_page(errorMessages=None):
    '''  
    Logout page
    '''
    logging.debug("IN display_logout_page()")
    context = get_default_context(request)

    # Clear authentication cookie and redirect user home page
    #resp = redirect('/')
    #resp.set_cookie(appconfig["application"]["auth_cookie_name"], '', expires=0)
    #expiry = ((datetime.utcnow() + timedelta(366)) - datetime(1970, 1, 1)).total_seconds()
    #bottle.response.set_cookie(appconfig["application"]["auth_cookie_name"], '', httponly=True, expires=0)
    remove_auth_cookie(AUTH_COOKIE_NAME)
    return redirect('/')
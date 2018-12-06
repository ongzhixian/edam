################################################################################
# Import statements
################################################################################

import logging
import os
import time
import urllib
import uuid
import bottle
import page_helpers

from datetime import datetime, timedelta

from bottle import default_app, run, route, request, response, redirect, abort
from app_helpers import appconfig

################################################################################
# Function decorators
################################################################################

def require_authentication(fn):
    logging.debug("IN require_authentication(%s)" % str(fn))
    def wrapper(*args, **kwargs):
        auth_cookie_id = request.cookies.get(appconfig["application"]["auth_cookie_name"])
        #ZX: KIV checksum checking until we need something more secure.
        #if auth_cookie_id and verify_cookie_checksum(auth_cookie_id):
        if auth_cookie_id:
            return fn(*args, **kwargs)
        login_url = "/login?from={0}".format(urllib.quote(request.url))
        redirect(login_url)
        return fn(*args, **kwargs)
    return wrapper
        
        # if not auth_cookie_id:
        #     logging.debug("IN auth cookie not exists")
        #     login_url = "/login?from={0}".format(urllib.quote(request.url))
        #     redirect(login_url)
        #     return fn(*args, **kwargs)
        # else:
        #     logging.debug("IN auth cookie exists")
        #     if verify_cookie_checksum(auth_cookie_id) == True:
        #         return fn(*args, **kwargs)
        #     else:
        #         login_url = "/login?from={0}".format(urllib.quote(request.url))
        #         redirect(login_url)
        #     return fn(*args, **kwargs)


################################################################################
# Basic functions
################################################################################


########################################
# Define idempotent functions
########################################

def get_hash(plain_text):
    hash_func = SHA256.new()
    hash_func.update(plain_text)
    return hash_func.hexdigest()


def calc_checksum(target_str):
    """ Calculate a checksum for a string (target_text)
    """
    logging.debug("IN calc_checksum()")
    sum = 0
    char_index = 1
    for c in target_str:
        sum = sum + (ord(c) * char_index)
        char_index = char_index + 1
    return sum


def calc_cookie_checksum(username, roles):
    logging.debug("IN calc_cookie_checksum()")
    username_checksum = calc_checksum(username) * 1
    roles_checksum = calc_checksum(roles) * 2
    return username_checksum + roles_checksum


def verify_cookie_checksum(cookie_body):
    logging.debug("IN verify_cookie_checksum()")
    parts = cookie_body.split("|")
    if len(parts) < 3:
        return False
    username = parts[0]
    roles = parts[1]
    check_sum = 0
    try:
        check_sum = int(parts[2])
    except ValueError:
        return False
    calc_val = calc_cookie_checksum(username, roles)
    if check_sum == calc_val:
        return True
    else:
        return False

def make_cookie_body(username, roles):
    check_sum = calc_cookie_checksum(username, roles)
    cookie_body = "%s|%s|%s" % (username, roles, check_sum)
    return cookie_body

def is_admin(roles):
    logging.info("IN is_admin")
    if roles is None:
        return False
    if isinstance(roles, list) == False:
        return False
    return "administrator" in roles.lower()


########################################
# Define application hooks
########################################

def add_auth_cookie(cookie_name):
    # Using UUID4 to generate cookie value
    new_uuid = uuid.uuid4()
    new_uuid_hex = new_uuid.hex
    # Set expiry to be a year (366 days) from now.
    expiry = ((datetime.utcnow() + timedelta(366)) - datetime(1970, 1, 1)).total_seconds()
    bottle.response.set_cookie(cookie_name, new_uuid.hex, httponly=True, expires=expiry)
    # Create a session folder; ZX: comment out; we cannot use this GAE
    # session_store_path = "./data/sessions/{0}".format(new_uuid_hex)
    # dir_exists = os.path.isdir(session_store_path)
    # if not dir_exists:
    #     os.mkdir(session_store_path)
    return new_uuid_hex

def remove_auth_cookie(cookie_name):
    bottle.response.set_cookie(cookie_name, '', httponly=True, expires=0)

def add_auth_cookie_hook():
    """Add auth cookie if user does not have auth cookie"""
    # Name of the cookie that we want to check for
    auth_cookie_name = str(appconfig['application']["auth_cookie_name"])
    # If cookie is NOT in request, generate cookie
    if auth_cookie_name not in bottle.request.cookies:
        add_auth_cookie(auth_cookie_name)
        # # Using UUID4 to generate cookie value
        # new_uuid = uuid.uuid4()
        # new_uuid_hex = new_uuid.hex
        # # Set expiry to be a year (366 days) from now.
        # expiry = ((datetime.utcnow() + timedelta(366)) - datetime(1970, 1, 1)).total_seconds()
        # bottle.response.set_cookie(auth_cookie_name, new_uuid.hex, httponly=True, expires=expiry)
        # # Create a session folder
        
        # session_store_path = "./data/sessions/{0}".format(new_uuid_hex)
        # dir_exists = os.path.isdir(session_store_path)
        # if not dir_exists:
        #     os.mkdir(session_store_path)


########################################
# Define core functions
########################################

def get_app():
    app = page_helpers.default_app()

    # add application hooks here
    # TODO: Add setup for add_auth_cookie_hook; it needs a sessions folder in data folder
    # Uncomment the below line to allow anonymous login
    # app.add_hook('after_request', add_auth_cookie_hook)
    return app

def get_default_context(request):
    context = {
        'auth_cookie'       : request.cookies.get(appconfig["application"]["auth_cookie_name"]),
        'current_datetime'  : datetime.now()
    }
    return context


################################################################################
# Variables dependent on Application basic functions
################################################################################

# N/A

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
################################################################################
# Modules and functions import statements
################################################################################

import pdb
from helpers.app_helpers import *
from helpers.page_helpers import *
from helpers.jinja2_helpers import *

from google.appengine.ext import ndb
# Import models
from models.test import Login,Account,Revision,Company

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
        
        # new_ent = Login()
        # new_ent.login_name = "zhixian"
        # new_ent.password = "password"
        # new_ent_key = new_ent.put()

        new_ent = Company()
        new_ent.name = "Brahman"
        new_ent_key = new_ent.put()

        if new_ent_key:
            logging.info("Record added")
        else:
            logging.info("No new entity key")
    return jinja2_env.get_template('html/test/home-page.html').render(context)


@route('/test/method2', method=['POST','GET'])
def display_register_page(errorMessages=None):
    context = get_default_context(request)
    try:
        if request.method == 'POST':
            logging.info("Testing method 2")
            #qry = Login.query().order()
            
            qry = Login.query(Login.login_name == "zhixian")
            qry_lst = qry.fetch(1)
            if qry_lst:
                logging.info("Has result. count is {0}".format(len(qry_lst)))
                if len(qry_lst) > 0:
                    res_obj = qry_lst[0]
                    # add another object with ancestry
                    new_ent = Login()
                    sandy_key = ndb.Key(Login, 'sandy@example.com')
                    new_ent.login_name = "sandy"
                    new_ent.password = "password"
                    new_ent.put()
                else:
                    logging.info("qry_lst length is less than 0")
            else:
                logging.info("No result from query.")
    except Exception as ex:
        logging.error(ex)

    return jinja2_env.get_template('html/test/home-page.html').render(context)


@route('/test/method3', method=['POST','GET'])
def display_method3(errorMessages=None):
    context = get_default_context(request)
    try:
        if request.method == 'POST':
            logging.info("Testing method 3")
            #qry = Login.query().order()
            
            qry = Login.query(Login.login_name == "zhixian")
            qry_lst = qry.fetch(1)
            if qry_lst:
                logging.info("Has result. count is {0}".format(len(qry_lst)))
                if len(qry_lst) > 0:
                    res_obj = qry_lst[0]
                    # add another object with ancestry
                    new_ent = Login()
                    sharlyn_key = ndb.Key(Login, 'sharlyn@example.com', parent=res_obj.key)
                    new_ent.login_name = "sharlyn"
                    new_ent.password = "password"
                    new_ent.put()
                else:
                    logging.info("qry_lst length is less than 0")
            else:
                logging.info("No result from query.")
    except Exception as ex:
        logging.error(ex)

    return jinja2_env.get_template('html/test/home-page.html').render(context)

@route('/test/method4', method=['POST','GET'])
def display_method4(errorMessages=None):
    context = get_default_context(request)
    try:
        if request.method == 'POST':
            logging.info("Testing method 4")
            # account = Account(username='Sandy', userid=1234, email='sandy@example.com', id='sandy@example.com')
            # account.put()
            # return account.key.id()  # returns 'sandy@example.com'

            # account_key = ndb.Key(Account, 'sandy@example.com')
            # #Ask Datastore to allocate an ID.
            # new_id = ndb.Model.allocate_ids(size=1, parent=account_key)[0]
            # # Datastore returns us an integer ID that we can use to create the message key
            # message_key = ndb.Key('Message', new_id, parent=account_key)
            # # Now we can put the message into Datastore
            # initial_revision = Revision(message_text='Hello', id='1', parent=message_key)
            # initial_revision.put()

            ancestry = []

            qry = Login.query(Login.login_name == "zhixian")
            qry_lst = qry.fetch(1)
            user1 = qry_lst[0]

            ancestry.append(user1.key.kind())
            ancestry.append(user1.key.id())
            # qry = Login.query(Login.login_name == "annie")
            # qry_lst = qry.fetch(1)
            # user2 = qry_lst[0]

            qry = Company.query(Company.name == "Brahman")
            qry_lst = qry.fetch(1)
            company1 = qry_lst[0]

            logging.info("Key kind:[{0}], id:[{1}]".format(company1.key.kind(), company1.key.id()))
            ancestry.append(company1.key.kind())
            ancestry.append(company1.key.id())

            logging.info(len(ancestry))

            #new_key = ndb.Key("Login", user1.key.id(), "Company", company1.key.id())
            new_key = ndb.Key(flat=ancestry)

            new_ent = Login(parent=new_key)
            new_ent.login_name = "mary"
            new_ent.password = "password"
            new_ent.put()
            # END if request.method == 'POST':
            
    except Exception as ex:
        logging.error(ex)

    return jinja2_env.get_template('html/test/home-page.html').render(context)

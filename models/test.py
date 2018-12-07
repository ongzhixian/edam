################################################################################
# Modules and functions import statements
################################################################################

import logging
import pdb
from helpers import *
from helpers.app_helpers import *
# from helpers.app_helpers import *
# from helpers.page_helpers import *
# from helpers.jinja2_helpers import *
# from helpers.mongodb_helpers import *
# from modules.scheduling import Roster
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from Crypto.Hash import SHA256
from datetime import datetime
from datetime import timedelta


################################################################################
# Available properties for defining ndb models

# IntegerProperty     BlobProperty        KeyProperty                 JsonProperty
# FloatProperty       DateTimeProperty    BlobKeyProperty             PickleProperty
# BooleanProperty     DateProperty        UserProperty                GenericProperty
# StringProperty      TimeProperty        StructuredProperty          ComputedProperty
# TextProperty        GeoPtProperty       LocalStructuredProperty 

# Common properties
# indexed   (bool)      default             verbose_name    (string)
# repeated  (bool)      choices     ([])    
# required  (bool)      validator   (func)  

# reference on modeling:
# https://cloud.google.com/appengine/articles/modeling#relationship-model

# https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#properties_and_value_types

# http://www.databaseanswers.org/data_models/

################################################################################
# Setup helper functions
################################################################################

# N/A

################################################################################
# Setup model classes
################################################################################

class TestModel:
    """aaa
    """

    def __init__(self):
        self.id = "id101"
        pass
    
    def GetId(self):
        return self.id

class Account(ndb.Model):
    username = ndb.StringProperty()
    userid = ndb.IntegerProperty()
    email = ndb.StringProperty()

class Revision(ndb.Model):
    message_text = ndb.StringProperty()


class Login(ndb.Model):
    login_name = ndb.StringProperty(required=True, indexed=True)
    password = ndb.StringProperty()

    @staticmethod
    def exists(login_name):
        query = Login.query(Login.login_name == login_name)
        result_list = query.fetch(1)
        if len(result_list) > 0:
            return True
        return False

    @staticmethod
    def add(login_name, password):
        new_ent = Login()
        new_ent.key = ndb.Key(Login, login_name)
        new_ent.login_name = login_name
        new_ent.password = password
        new_ent_key = new_ent.put()
        return new_ent_key

    @staticmethod
    def register_login2(urlsafe_key, quantity):
        blazer_size_key = ndb.Key(urlsafe=urlsafe_key)
        blazer_size = blazer_size_key.get()
        last_registered_number = blazer_size.last_registered_number

########################################
# Generic models
########################################

class Article(ndb.Model):
    title = ndb.StringProperty()
    stars = ndb.IntegerProperty()
    tags = ndb.StringProperty(repeated=True)

class Task(ndb.Model):
    title = ndb.StringProperty()
    stars = ndb.IntegerProperty()
    tags = ndb.StringProperty(repeated=True)
    
class Group(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()

class Address(ndb.Model):
    type = ndb.StringProperty()  # E.g., 'home', 'work', 'billing', 'lading'
    line1 = ndb.StringProperty()
    line2 = ndb.StringProperty()
    line3 = ndb.StringProperty()
    line4 = ndb.StringProperty()
    number_of_lines = ndb.IntegerProperty()
    # street = ndb.StringProperty()
    # city = ndb.StringProperty()


##### Example of polyModel
class Contact(polymodel.PolyModel):
    # phone_number = ndb.PhoneNumberProperty()
    # address = ndb.PostalAddressProperty()
    type_name = ndb.StringProperty()
    pass

class PersonContact(Contact):
    first_name1 = ndb.StringProperty()
    last_name2 = ndb.StringProperty()
    #mobile_number = ndb.PhoneNumberProperty()

class CompanyContact(Contact):
    name = ndb.StringProperty()
    #fax_number = ndb.PhoneNumberProperty()



# class Contact(db.Model):
#     # ID of user that owns this entry.
#     owner = db.StringProperty()

#     # Basic info.
#     name = db.StringProperty()
#     birth_day = db.DateProperty()

#     # Address info.
#     address = db.PostalAddressProperty()

#     # Company info.
#     company_title = db.StringProperty()
#     company_name = db.StringProperty()
#     company_description = db.StringProperty()
#     company_address = db.PostalAddressProperty()

#     # Group affiliation
#     groups = db.ListProperty(db.Key)

class UserRoles(ndb.Model):
    pass


class PersonalProfile(ndb.Model):
    first_name = ndb.StringProperty(required=False)
    last_name = ndb.StringProperty(required=False)
    display_name = ndb.StringProperty(required=False)
    national_id = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=True)
    access = ndb.KeyProperty(kind=Group, repeated=True)
    login = ndb.KeyProperty(kind=Login, repeated=True)

    @staticmethod
    def exists(login_key):
        try:
            #query = Article.query(Article.tags.IN(['python', 'ruby', 'php']))
            search_key = ndb.Key(Login, login_key)
            logging.info("In PersonalProfile exists")
            query = PersonalProfile.query(PersonalProfile.login.IN([search_key]))
            logging.info("get query")
            result_list = query.fetch(1)
            logging.info("fetch")
            if len(result_list) > 0:
                logging.info("return true")
                return True
            logging.info("return false")
            return False
        except Exception as ex:
            logging.error(ex)




class Employee(ndb.Model):
    """A model representing an employee."""
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    display_name = ndb.StringProperty(required=True)
    national_id = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    #company = ndb.KeyProperty(Company)
    contacts = ndb.KeyProperty(kind=Contact, repeated=True)
    #contacts = ndb.StructuredProperty(PersonContact, repeated=True)



class Company(ndb.Model):
    """A model representing a company."""
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    company_address = ndb.StringProperty()
    preferred_address = ndb.KeyProperty(Address)
    addresses = ndb.KeyProperty(kind=Address, repeated=True)
    employees = ndb.KeyProperty(kind=Employee, repeated=True)
    #contacts = ndb.StructuredProperty(Contact, repeated=True)
    # TODO: method to add address
    # TODO: method to add employee
    
    @staticmethod
    def exists(name):
        query = Company.query(Company.name == name)
        result_list = query.fetch(1)
        if len(result_list) > 0:
            return True
        return False

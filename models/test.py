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
from Crypto.Hash import SHA256
from datetime import datetime
from datetime import timedelta

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
    login_name = ndb.StringProperty()
    password = ndb.StringProperty()

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
    
class Group(db.Model):
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
    phone_number = ndb.PhoneNumberProperty()
    address = ndb.PostalAddressProperty()

class PersonContact(Contact):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    mobile_number = ndb.PhoneNumberProperty()

class CompanyContact(Contact):
    name = ndb.StringProperty()
    fax_number = ndb.PhoneNumberProperty()


class UserProfile(ndb.Model):
    access = ndb.KeyProperty(kind=Group, repeated=True)


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

class Company(ndb.Model):
    """A model representing a company."""
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    company_address = ndb.StringProperty()
    preferred_address = ndb.KeyProperty(Address)
    addresses = ndb.StructuredProperty(Address, repeated=True)
    contacts = ndb.StructuredProperty(Contact, repeated=True)


class Employee(ndb.Model):
    """A model representing an employee."""
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    display_name = ndb.StringProperty(required=True)
    national_id = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    company = ndb.KeyProperty(Company)
    #contacts = ndb.StructuredProperty(Contact, repeated=True)
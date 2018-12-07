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

class Company(ndb.Model):
    """A model representing a company."""
    name = ndb.StringProperty(required=True)
    full_name = ndb.StringProperty(required=True)
    abbreviation = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    registration_number = ndb.IntegerProperty(default=-1, required=True)
    registration_date = ndb.DateProperty(default=None)

    @staticmethod
    def get_all():
        result = []
        query = Company.query().order(Company.name)
        for rec in query:
            result.append({
                'key' : rec.key.urlsafe(),
                'name' : rec.name,
                'full_name' : rec.full_name,
                'abbreviation' : rec.abbreviation,
                'description' : rec.description,
                'registration_date' : rec.registration_date
            })
        return result

################################################################################
# Setup model classes
################################################################################

# Available properties for defining ndb models

# IntegerProperty     BlobProperty        KeyProperty                 JsonProperty
# FloatProperty       DateTimeProperty    BlobKeyProperty             PickleProperty
# BooleanProperty     DateProperty        UserProperty                GenericProperty
# StringProperty      TimeProperty        StructuredProperty          ComputedProperty
# TextProperty        GeoPtProperty       LocalStructuredProperty 

class Login(ndb.Model):
    email = ndb.StringProperty(required=True)
    password_salt = ndb.StringProperty(required=True)
    password_hash = ndb.StringProperty(required=True)
    last_login_datetime = ndb.DateTimeProperty(required=False)
    last_password_update_datetime = ndb.DateTimeProperty(required=False)
    login_attempts_left = ndb.IntegerProperty(default=6, required=True)
    creation_timestamp = ndb.DateTimeProperty()

    @staticmethod
    def get_hash(plain_text):
        hash_func = SHA256.new()
        hash_func.update(plain_text)
        return hash_func.hexdigest()

    @staticmethod
    def get_salt():
        return "GEN0"

    @staticmethod
    def register_login(email, password):
        new_ent = Login()
        new_ent.email = email
        new_ent.password_salt = Login.get_salt()
        new_ent.password_hash = Login.get_hash(new_ent.password_salt + password)
        new_ent.last_login_datetime = None
        new_ent.last_password_update_datetime = None
        new_ent.login_attempts_left = 6
        return new_ent.put()

# class UserProfile(ndb.Model):
#     new_ent.roles = ['administrator']
#     username = ndb.StringProperty(required=True)
#     password = ndb.StringProperty(required=True)
#     roles = ndb.StringProperty(repeated=True)
#     create_datetime = DateTimeProperty(required=True)
#     last_login_datetime = DateTimeProperty(required=False)
#     last_password_update_datetime = DateTimeProperty(required=False)
#     timestamp = ndb.DateTimeProperty()
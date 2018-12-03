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

from app_helpers import appconfig
from pymongo import MongoClient

################################################################################
# Function decorators
################################################################################

# N/A

################################################################################
# Basic functions
################################################################################

########################################
# Define core functions
########################################

def get_mongodb(db_name):
    logging.info("IN get_mongodb looking for {0}".format(db_name))
    if "mongodb" not in appconfig:
        return None
    if db_name not in appconfig["mongodb"]:
        return None
    db_cfg = appconfig["mongodb"][db_name]
    #logging.info(db_cfg)
    connection_string = "mongodb://{0}:{1}@{2}:{3}/{4}".format(
        db_cfg["username"], 
        db_cfg["password"], 
        db_cfg["hostname"], 
        db_cfg["port"], 
        db_cfg["database"])
    client = MongoClient(connection_string)
    db = client[db_name]
    return db
    

########################################
# Define helper functions
########################################

# N/A

################################################################################
# Variables dependent on Application basic functions
################################################################################

# N/A

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
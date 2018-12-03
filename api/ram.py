import json
import logging
import os
from helpers.page_helpers import *

################################################################################
# Setup helper functions
################################################################################

# N/A

################################################################################
# Setup routes
################################################################################

@route('/api/ram/register/resource-type', method='POST')
def api_register_resource_type():
    logging.debug("IN api_register_resource_type")
    # json_data = request.json
    # logging.info(str(json_data))
    cwd = os.getcwd()
    logging.info(cwd)


# @route('/api/sample')
# def api_sample_get():
#     logging.debug("IN api_sample_get")
#     return "['Hello', 'World']"
    
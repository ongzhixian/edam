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

@route('/api/ping', method=['GET','POST'])
def api_ping():
    """API to let a CRON job just keep pinging this application every 5 minutes."""
    logging.debug("IN api_ping_post")
    return


# @route('/api/sample')
# def api_sample_get():
#     logging.debug("IN api_sample_get")
#     return "['Hello', 'World']"
    
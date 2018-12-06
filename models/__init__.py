################################################################################
# Define package composition
################################################################################

import os

################################################################################
# Define package composition
################################################################################

if 'SERVER_SOFTWARE' in os.environ:
    __all__ = ["demo", "test"]
    #https://cloud.google.com/appengine/docs/standard/python/how-requests-are-handled#environment
else:
    __all__ = ["demo", "test"]
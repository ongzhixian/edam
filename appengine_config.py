# Import Python libraries in "lib" folder to App Engine
# This is for libraries that are not built-in App Engine
# For a list of App Engine built-in libraries see the below link
# https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')

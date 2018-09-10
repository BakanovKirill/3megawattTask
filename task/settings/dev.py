from settings.base import *

DEBUG = True
# Debug toolbar config
if DEBUG:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE
    INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar', ]

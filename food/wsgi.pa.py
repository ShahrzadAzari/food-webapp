import os
import sys
# add your project directory to the sys.path
project_home = u'/home/98521018/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)
# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'food.settings'
# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
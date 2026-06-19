import sys
import os

# Add the project root to Python path so 'myProject13' package is found
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject13.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import os
import sys

# Add your project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HNG_Task1.settings")

app = get_wsgi_application()
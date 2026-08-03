import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fortune_classical_college.config.production')

application = get_wsgi_application()

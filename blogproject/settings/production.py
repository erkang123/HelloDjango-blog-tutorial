from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']



DEBUG = False

ALLOWED_HOSTS = ['.kanryblog.com']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch:9200/'

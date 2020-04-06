from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_blog',
        'USER':'root',
        'PASSWORD':'123456a',
        'HOST':'db',
        'PORT':3306,
        'OPTIONS': {'charset': 'utf8'},
    }
}

DEBUG = False

ALLOWED_HOSTS = ['*']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_tutorial_elasticsearch:9200/'

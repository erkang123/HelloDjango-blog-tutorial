from .common import *

SECRET_KEY = '8xkq_+yhixuo9419#r1gf7k$2q!ywroi+%j0db1-2zodrln9^%'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'

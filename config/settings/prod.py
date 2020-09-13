from .base import *

ALLOWED_HOSTS = ['52.79.97.52']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []

DEBUG = False # 오류 발생시 정보를 노출하지 않기 위함
from .common import *

INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]


INTERNAL_IPS = ['127.0.0.1']
from .settings import *


DEBUG=True

ALLOWED_HOSTS=['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mymemoblog',
        'USER': 'root',
        'HOST': '',
        'PORT': '',
    }
}
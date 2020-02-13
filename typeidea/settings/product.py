from .base import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'idea_db',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

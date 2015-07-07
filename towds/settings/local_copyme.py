import os
import sys
from .settings import *

SECRET_KEY = #Local Secret Key goes here

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Put local Database info here

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

ALLOWED_HOSTS = [
    'localhost', # Allow domain and subdomains
]


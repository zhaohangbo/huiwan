#!/usr/bin/python

import os
from unipath import Path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print 'BASE_DIR is : ',BASE_DIR

PROJECT_DIR = Path(__file__).parent

print 'PROJECT_DIR is : ', PROJECT_DIR

STATIC_ROOT = PROJECT_DIR.parent.parent.child('static')

print 'STATIC_ROOT is : ', STATIC_ROOT 

STATICFILES_DIRS = (
            PROJECT_DIR.child('static'),
)

print 'PROJECT_DIR.child(static) is : ',  PROJECT_DIR.child('static')
print 'PROJECT_DIR.child(templates) is : ',  PROJECT_DIR.child('templates'),

ROOT_URLCONF = 'huiwan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                PROJECT_DIR.child('templates'),
                ],
        'APP_DIRS': True,
    },
]

STATIC_URL = '/static/'


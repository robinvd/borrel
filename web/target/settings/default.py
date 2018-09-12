# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.pardir)

PROJECT_DIR = lambda base: os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', base).replace('\\', '/'))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%>R4vq?[sD&mjV[e-KO(|G/ULP55n{x4zX7ki04z$I;1SC-,Rq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SITE_ID = 1

ADMINS = (('Target Holding B.V.', 'huub.segers@target-holding.nl'),)

DEFAULT_FROM_EMAIL = 'huub.segers@target-holding.nl'
DEFAULT_TO_EMAIL = DEFAULT_FROM_EMAIL
FROM_EMAIL = DEFAULT_FROM_EMAIL
CONTACT_EMAIL = 'huub.segers@target-holding.nl'

## These are default TGHO
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	
	'polymorphic',
	'sekizai',
	'admin_tools',
	
	'target',
	'target.frontend',
	'target.borrel',
]

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',  # Required by Django-CMS
	'django.middleware.common.CommonMiddleware',
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'data', 'tgho.sqlite3'),
	}
}

# order defines priority
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',  # default backend
)

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = '/'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'target/frontend/templates/'),
		],
		'OPTIONS': {
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
				'sekizai.context_processors.sekizai',
			],
			'loaders': [
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
				'admin_tools.template_loaders.Loader',
			]
		},
	},
]

WSGI_APPLICATION = 'target.wsgi.application'

ROOT_URLCONF = 'target.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOGGING = {
	'version': 1,
	
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
		},
	},
	
	'loggers': {
		'target': {
			'level': 'INFO',
			'propagate': True,
		},
	},
}

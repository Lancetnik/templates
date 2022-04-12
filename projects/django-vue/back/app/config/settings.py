import os
from pathlib import Path
from datetime import timedelta

from corsheaders.defaults import default_headers
import yaml


CONFIG_DIR = Path(__file__).resolve().parent
BASE_DIR = CONFIG_DIR.parent


def read_config(file: Path) -> dict:
    try:
        with file.open() as ymlfile:
            data = yaml.safe_load(ymlfile)
        return data
    except FileNotFoundError as e:
        print(f"WARNING: {e}")
        return {}

config = read_config(CONFIG_DIR / 'config.yml')


SECRET_KEY = os.environ.get('SECRET_KEY', default=config.get('SECRET_KEY', 'debug-secret-key'))

DEBUG = os.environ.get('DEBUG', default=config.get('DEBUG', True))

ALLOWED_HOSTS = tuple({
    '0.0.0.0', '127.0.0.1', 'localhost'
})


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework.authtoken',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'djoser',
    'drf_yasg'
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
         'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer','JWT'),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'ALLOW-FROM http://localhost:8080/'

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = "config.asgi.application"

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

db = config.get("POSTGRES", {})
POSTGRES_NAME = os.environ.get('POSTGRES_DB', default=db.get("DB"))
POSTGRES_USER = os.environ.get('POSTGRES_USER', default=db.get("USER", "user"))
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default=db.get("PASSWORD", "password"))
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default=db.get("HOST", "localhost"))
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', default=db.get("PORT", "5432"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2' if POSTGRES_NAME else "django.db.backends.sqlite3",
        'NAME': POSTGRES_NAME or str(BASE_DIR / "db.sqlite3"),
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   str(BASE_DIR / "index" / "static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (str(BASE_DIR / "index" / "templates"),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS  =  list(default_headers)  +  [ 
    'Content-Disposition', 
]

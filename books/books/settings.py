"""
Django settings for books project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-cqf1dfojy6tc8t#xcqwv=9wmk1yy-*1+8t0167r8i5!*)rii9s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # дефолтные приложения django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ДОБАВЛЕННЫЕ МОДУЛИ
    # фильтрация возвращемых значений из django rest
    "django_filters",
    # настройки для django-social-auth, добавляет аунтентификацию пользователей через социальные сети
    "social_django",
    # ----------------------------------------------
    # МОИ ПРЕЛОЖЕНИЯ
    "store",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "books.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "books.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# ПОДКЛЮЧЕНИЕ К БД SQLITE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# ПОДКЛЮЧЕНИЕ К БД POSTGRESQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "books_db",
        "USER": "postgres",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# НАСТРОЙКИ ДЛЯ DJANGO REST
# указываем обработку страниц для django rest по умолчанию в формате json
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}


# НАСТРОЙКИ ДЛЯ DJANGO-SOCIAL-AUTH
SOCIAL_AUTH_JSONFIELD_ENABLED = True
AUTHENTICATION_BACKENDS = (
    # аутентификация пользователя через Git Hub
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
SOCIAL_AUTH_URL_NAMESPACE = "social"

# НАСТРОЙКИ ДЛЯ DJANGO-SOCIAL-AUTH ДЛЯ УАТЕНТИФКАЦИИ ЧЕРЕЗ GIT HUB
# заначения берем из зарегистрированого приложения OAuth Apps в Developer Settings на Git Hub
SOCIAL_AUTH_GITHUB_KEY = "Ov23lifGqSHPl6mtft2x"
SOCIAL_AUTH_GITHUB_SECRET = "0322c776a6f26172813c839545cbab888e560e3c"


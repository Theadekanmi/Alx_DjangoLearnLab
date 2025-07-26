"""
Django settings for advanced_features_and_security project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9(2-40d0hy40(%p(ltdkiyr-kzqv38)rjhgm4-9+ej23!@ss8='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Set to False in production!

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # This is YOUR custom user app for THIS project
    'csp',       # For Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware', # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'advanced_features_and_security.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'advanced_features_and_security.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/topics/static-files/

STATIC_URL = 'static/'

# Media files (for profile photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tell Django to use our custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Browser-side protections
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY' # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True # Prevents browsers from MIME-sniffing content

# Enforce secure cookies (requires HTTPS)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# HSTS settings (only enable in production with HTTPS)
SECURE_SSL_REDIRECT = True # Redirects HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Make cookies HTTP-only (prevents JavaScript access)
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# Content Security Policy (CSP) settings for django-csp v4.0+
# This is the new dictionary format.
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src': ("'self'", "'unsafe-inline'",), # 'unsafe-inline' often needed for development
        'style-src': ("'self'", "'unsafe-inline'",),  # 'unsafe-inline' often needed for development
        'img-src': ("'self'", "data:",),
        'font-src': ("'self'",),
        'connect-src': ("'self'",),
        'frame-ancestors': ("'self'",), # Prevents embedding your site in iframes by other sites
        'object-src': ("'none'",), # Disallow <object>, <embed>, <applet>
        'base-uri': ("'self'",), # Restricts URLs that can be used in <base> element
        'form-action': ("'self'",), # Restricts URLs that can be used as the target of form submissions
    },
    # Optional: Report-Only mode (useful for testing CSP without blocking content)
    # 'REPORT_ONLY': True,
    # 'REPORT_URI': ('/csp-report/',), # You would need a view to handle these reports
}

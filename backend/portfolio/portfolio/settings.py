import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Base directory
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*"]  # Safe for portfolio (restrict later if needed)

CSRF_TRUSTED_ORIGINS = [
    "https://*.koyeb.app",
]

# --------------------------------------------------
# Application definition
# --------------------------------------------------
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "corsheaders",
    "django_filters",

    # Local apps
    "core",
    "api",
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# URLs & WSGI
# --------------------------------------------------
ROOT_URLCONF = "portfolio.urls"

WSGI_APPLICATION = "portfolio.wsgi.application"

# --------------------------------------------------
# Templates
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# --------------------------------------------------
# Database
# --------------------------------------------------
if os.environ.get("DATABASE_URL"):
    # Production (Koyeb / Cloud)
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ["DATABASE_URL"],
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    # Local Docker
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME", "my_portfolio"),
            "USER": os.environ.get("DB_USER", "postgres"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "admin"),
            "HOST": os.environ.get("DB_HOST", "db"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }

# --------------------------------------------------
# REST Framework
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# --------------------------------------------------
# CORS
# --------------------------------------------------
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://your-frontend-domain.com",
    ]

# --------------------------------------------------
# Static files (WhiteNoise)
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# --------------------------------------------------
# Media files
# --------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# Internationalization
# --------------------------------------------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Default primary key field type
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

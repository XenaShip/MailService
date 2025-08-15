from pathlib import Path
import os

# ——— БАЗА ————————————————————————————————————————————————————————————————
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = os.getenv("DEBUG", "True").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if h.strip()]

# ——— ПРИЛОЖЕНИЯ ————————————————————————————————————————————————————————
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "mail",
    "blog",
    "users",
]

# ——— МИДДЛВАРЬ ————————————————————————————————————————————————————————
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ——— TEMPLATES ————————————————————————————————————————————————————————————
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # папка для общих шаблонов; шаблоны внутри приложений тоже найдутся через APP_DIRS
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

WSGI_APPLICATION = "config.wsgi.application"

# ——— БАЗА ДАННЫХ ————————————————————————————————————————————————————————

if os.getenv("DB_NAME"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ——— ПАРОЛИ ———————————————————————————————————————————————————————————————
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ——— ЛОКАЛЬ / ВРЕМЯ ———————————————————————————————————————————————————————
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Amsterdam"
USE_I18N = True
USE_TZ = True

# ——— СТАТИКА / МЕДИА ————————————————————————————————————————————————————
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"      # для collectstatic (на проде)
STATICFILES_DIRS = [BASE_DIR / "static"]    # твоя папка со статикой (на деве, опционально)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ——— АУТЕНТИФИКАЦИЯ —————————————————————————————————————————————————————

AUTH_USER_MODEL = os.getenv("AUTH_USER_MODEL", "users.User")

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# ——— БЕЗОПАСНОСТЬ (минимум для прод-стенда) ————————————————————————————
if not DEBUG:
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "31536000"))
    SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True").lower() == "true"
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "True").lower() == "true"
    CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "True").lower() == "true"

# Если будешь открывать из браузера по нестандартному домену — пропиши его тут
CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()
]

# ——— ЛОГИРОВАНИЕ (удобное по умолчанию) ——————————————————————————————————
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[{levelname}] {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO", "propagate": False},
    },
}

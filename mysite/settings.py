from pathlib import Path
import os

# Podstawowa ścieżka projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Klucz bezpieczeństwa (możesz zostawić ten lub swój oryginalny)
SECRET_KEY = 'django-insecure-twoja-unikalna-klucz-zostaw-swoj-jesli-chcesz'

# Tryb debugowania włączony dla potrzeb tutorialu
DEBUG = True

ALLOWED_HOSTS = []

# Rejestracja Twojej aplikacji 'polls' - KLUCZOWE dla szablonów
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, # To mówi Django, by szukało folderu 'templates' w aplikacjach
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Konfiguracja bazy danych SQLite - TO NAPRAWI BŁĄD "NAME"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Walidacja haseł
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Ustawienia językowe i czasu
LANGUAGE_CODE = 'pl-pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_TZ = True

# Pliki statyczne (CSS, obrazy)
STATIC_URL = 'static/'

# Domyślny typ klucza głównego
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
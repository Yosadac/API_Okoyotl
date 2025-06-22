import os
import dj_database_url
from dotenv import load_dotenv
from datetime import timedelta
from pathlib import Path  # Agrega esta línea

# Agrega esta definición de BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Usa una variable de entorno para la SECRET_KEY
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-9*z9%1_&)m%u7_!d$@_(4o2u@3$r+-=3^n@1tbr6dj#$!@9=+b')

# Configuración de bases de datos usando variables de entorno
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'postgres://postgres.oarlvtewarfcvndbhqsq:MiztliG16y03@aws-0-us-east-2.pooler.supabase.com:6543/postgres'),
        conn_max_age=600
    )
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # para que no requiera login
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}


# Configuración de JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Configuración de correo electrónico (ejemplo con SendGrid)
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = True

# O si prefieres Mailgun:
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# ANYMAIL = {
#     "MAILGUN_API_KEY": os.getenv('MAILGUN_API_KEY'),
#     "MAILGUN_SENDER_DOMAIN": os.getenv('MAILGUN_DOMAIN'),
# }

# Configuración de CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Para desarrollo con React
    "http://127.0.0.1:3000",
]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_celery_results',
    'django_celery_beat',
    # Local
    'Okoyotl',
]

# Middleware
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

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Ahora BASE_DIR está definido

# Configuración de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Agrega esta línea si usas uploads de archivos

# Configuración de seguridad para producción
if os.getenv('ENVIRONMENT') == 'production':
    DEBUG = False
    ALLOWED_HOSTS = ['.yourdomain.com', 'your-render-app.onrender.com']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
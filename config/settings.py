from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# CẤU HÌNH CHUNG
# =========================

# Khi chạy Docker, khóa bí mật được lấy từ biến môi trường
# DJANGO_SECRET_KEY trong file .env.
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'dev-only-change-me'
)

DEBUG = os.getenv(
    'DJANGO_DEBUG',
    'False'
).lower() == 'true'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'django',
]


# =========================
# ỨNG DỤNG
# =========================

INSTALLED_APPS = [
    'django_prometheus',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'students',
]


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_prometheus.middleware.PrometheusAfterMiddleware',
]


ROOT_URLCONF = 'config.urls'


# =========================
# TEMPLATE
# =========================

TEMPLATES = [
    {
        'BACKEND':
            'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# =========================
# CƠ SỞ DỮ LIỆU MYSQL
# =========================
# Chạy trực tiếp Windows:
#   DB_HOST=127.0.0.1
#   DB_PORT=3307
#
# Chạy bằng Docker:
#   DB_HOST=mysql
#   DB_PORT=3306
#
# Mật khẩu không ghi trực tiếp trong mã nguồn.
# Docker lấy DB_PASSWORD từ file .env.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': os.getenv(
            'DB_NAME',
            'quan_ly_sinh_vien'
        ),

        'USER': os.getenv(
            'DB_USER',
            'qlsv_user'
        ),

        'PASSWORD': os.getenv(
            'DB_PASSWORD',
            ''
        ),

        'HOST': os.getenv(
            'DB_HOST',
            '127.0.0.1'
        ),

        'PORT': os.getenv(
            'DB_PORT',
            '3307'
        ),

        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}


# =========================
# KIỂM TRA MẬT KHẨU
# =========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator',
    },
]


# =========================
# NGÔN NGỮ VÀ THỜI GIAN
# =========================

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# =========================
# FILE TĨNH
# =========================

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# EMAIL
# =========================

EMAIL_BACKEND = (
    'django.core.mail.backends.console.EmailBackend'
)


# =========================
# CẤU HÌNH BẢO MẬT
# =========================

# Ngăn trình duyệt tự suy đoán kiểu nội dung.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Chỉ gửi thông tin referrer trong cùng website.
SECURE_REFERRER_POLICY = 'same-origin'

# Chống website khác nhúng trang vào iframe.
X_FRAME_OPTIONS = 'DENY'

# JavaScript không được truy cập cookie phiên đăng nhập.
SESSION_COOKIE_HTTPONLY = True

# Chính sách SameSite cho cookie phiên.
SESSION_COOKIE_SAMESITE = 'Lax'

# Chính sách SameSite cho cookie CSRF.
CSRF_COOKIE_SAMESITE = 'Lax'

# Cookie chỉ được truyền qua HTTPS.
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# Django nhận biết HTTPS do Nginx reverse proxy chuyển tiếp.
SECURE_PROXY_SSL_HEADER = (
    'HTTP_X_FORWARDED_PROTO',
    'https',
)

# Cho phép biểu mẫu gửi dữ liệu từ website HTTPS.
CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8443',
]
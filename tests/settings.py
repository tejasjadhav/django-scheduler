
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'sb_my=bgdzf6u-5^k=tyzo)+tu)s+gya&9!wn(8oynkr=d&6un'

INSTALLED_APPS = [
    'scheduler',
]

MIDDLEWARE = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

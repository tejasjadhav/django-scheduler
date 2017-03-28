import os
import sys

import django

from tests.runner import TestRunner

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()
    failures = TestRunner().run_tests(['tests.tests'])
    sys.exit(bool(failures))

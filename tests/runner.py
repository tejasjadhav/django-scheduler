TestRunner = None

try:
    # Django <= 1.8
    from django.test.simple import DjangoTestSuiteRunner
    TestRunner = DjangoTestSuiteRunner
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner
    TestRunner = DiscoverRunner

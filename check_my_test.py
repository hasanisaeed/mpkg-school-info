# school_info/check_my_test.py
import sys
from unittest import TestSuite
from boot_my_app import boot_my_app

boot_my_app()

labels = ["my_app.tests", ]


def get_suite(labels=None):
    if labels is None:
        labels = labels
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)
    return TestSuite()


if __name__ == "__main__":
    labels = labels
    if len(sys.argv[1:]) > 0:
        labels = sys.argv[1:]
    get_suite(labels)

# import sys
# from unittest import TestSuite
#
# from boot_my_app import boot_my_app
#
# boot_my_app()
#
# my_test = ["my_app.tests", ]
#
#
# def get_suite(labels=None):
#     if labels is None:
#         labels = my_test
#     from django.test.runner import DiscoverRunner
#     runner = DiscoverRunner(verbosity=1)
#     failures = runner.run_tests(labels)
#     if failures:
#         sys.exit(failures)
#
#     return TestSuite()

# my_app/tests.py
from django.test import TestCase
from .models import School


class SchoolTest(TestCase):
    fixtures = ["fake.json", ]

    def test_average_school(self):
        school = School.objects.get(id=1)
        average = school.average()

        # مقداری که من انتظار دارم دریافت کنم
        ext_avg = "19.24"
        self.assertEqual(ext_avg, average)



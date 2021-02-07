# my_app/models.py
from django.db import models
from docutils.nodes import math


class School(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"School = {self.name}, Average: {self.average()}"

    def average(self):
        # برای اینکه تا دو رقم اعشار میخوام میانگین رو برگردونه این کار رو کردم.
        return "{:.2f}".format(sum(student.average for student in self.student_set.all())
                               / self.student_set.count())


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    name = models.CharField(max_length=20, null=False, blank=False)
    average = models.FloatField()

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average}"


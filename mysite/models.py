from django.db import models
from django.urls import reverse

class StudentGroup(models.Model):
    group = models.CharField(max_length=10)
    entry_year = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.group

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    info = models.ForeignKey(StudentGroup(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create_student")
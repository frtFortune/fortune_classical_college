from django.db import models
from django.conf import settings


class AcademicTerm(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=50, unique=True, blank=True)
    class_group = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if self.admission_number:
            return f"{name} ({self.admission_number})"
        return name

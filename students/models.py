from django.db import models
from django.conf import settings


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
    # TODO: class_group is a temporary association for Module 2.
    # In Module 3 this should be replaced by an explicit StudentEnrollment model
    # that records session-based enrollment events and supports transfers.
    class_group = models.ForeignKey(
        'academics.SchoolClass',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if self.admission_number:
            return f"{name} ({self.admission_number})"
        return name

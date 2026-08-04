from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


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
    # Deprecated compatibility field retained while the system transitions to
    # historical StudentEnrollment records for session-based class placement.
    class_group = models.ForeignKey(
        'academics.SchoolClass',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='deprecated_students',
        help_text='Deprecated: use StudentEnrollment for historical, session-based placement.',
    )

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if self.admission_number:
            return f"{name} ({self.admission_number})"
        return name


class StudentEnrollment(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        COMPLETED = 'COMPLETED', 'Completed'
        LEFT = 'LEFT', 'Left'
        TRANSFERRED = 'TRANSFERRED', 'Transferred'
        REPEATED = 'REPEATED', 'Repeated'
        SUSPENDED = 'SUSPENDED', 'Suspended'

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='enrollments',
    )
    session = models.ForeignKey(
        'academics.AcademicSession',
        on_delete=models.PROTECT,
        related_name='student_enrollments',
    )
    school_class = models.ForeignKey(
        'academics.SchoolClass',
        on_delete=models.PROTECT,
        related_name='student_enrollments',
    )
    date_joined = models.DateField(null=True, blank=True)
    date_left = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_joined', 'student__last_name', 'student__first_name']
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'session'],
                name='unique_student_session_enrollment',
            )
        ]

    # TODO: Move promotion, repeating, transfer, and graduation workflows into service classes.
    # Keep business logic out of models and admin so the architecture remains extensible.
    def clean(self):
        super().clean()
        if self.session_id and self.school_class_id and self.session_id != self.school_class.session_id:
            raise ValidationError('The selected AcademicSession and SchoolClass must belong to the same academic session.')

    def __str__(self):
        return f"{self.student} -> {self.school_class} ({self.session})"


class StudentSubject(models.Model):
    # Internal data model for historical subject assignment.
    # Future administrators will assign subjects through bulk spreadsheet-like workflows rather than editing this model one record at a time.
    student_enrollment = models.ForeignKey(
        StudentEnrollment,
        on_delete=models.PROTECT,
        related_name='subjects',
    )
    class_subject = models.ForeignKey(
        'academics.ClassSubject',
        on_delete=models.PROTECT,
        related_name='student_subjects',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['student_enrollment__student__last_name', 'student_enrollment__student__first_name', 'class_subject__subject__name']
        constraints = [
            models.UniqueConstraint(fields=['student_enrollment', 'class_subject'], name='unique_student_subject_per_enrollment')
        ]

    def clean(self):
        super().clean()
        if self.student_enrollment_id and self.class_subject_id:
            enrollment_class = self.student_enrollment.school_class
            if self.class_subject.school_class_id != enrollment_class.id:
                raise ValidationError('The selected ClassSubject must belong to the same SchoolClass as the enrollment.')

    # TODO: Future report cards should become immutable snapshot records.
    # They must not depend on a student's live enrollment or current subject assignments after approval.
    def __str__(self):
        return f"{self.class_subject.subject} for {self.student_enrollment}"

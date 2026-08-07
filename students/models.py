from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    class AdmissionType(models.TextChoices):
        NEW = "NEW", "New Admission"
        TRANSFER = "TRANSFER", "Transfer"
        RETURNING = "RETURNING", "Returning"

    class StudentStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        GRADUATED = "GRADUATED", "Graduated"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"
        TRANSFERRED = "TRANSFERRED", "Transferred"
        SUSPENDED = "SUSPENDED", "Suspended"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
        null=True,
        blank=True,
    )

    admission_number = models.CharField(
        max_length=50,
        unique=True,
    )

    first_name = models.CharField(max_length=100)

    other_names = models.CharField(
        max_length=200,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    place_of_birth = models.CharField(
        max_length=150,
        blank=True,
    )

    nationality = models.CharField(
        max_length=100,
        blank=True,
    )

    state_of_origin = models.CharField(
        max_length=100,
        blank=True,
    )

    local_government_area = models.CharField(
        max_length=100,
        blank=True,
    )

    tribe = models.CharField(
        max_length=100,
        blank=True,
    )

    passport = models.ImageField(
        upload_to="students/passports/",
        null=True,
        blank=True,
    )

    admission_date = models.DateField(
        null=True,
        blank=True,
    )

    previous_school = models.CharField(
        max_length=250,
        blank=True,
    )

    admission_type = models.CharField(
        max_length=20,
        choices=AdmissionType.choices,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVE,
    )

    # Deprecated compatibility field
    class_group = models.ForeignKey(
        "academics.SchoolClass",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deprecated_students",
        help_text="Deprecated. Use StudentEnrollment.",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.other_names} ({self.admission_number})"


class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    residential_address = models.TextField(blank=True)

    religion = models.CharField(
        max_length=100,
        blank=True,
    )

    student_phone = models.CharField(
        max_length=30,
        blank=True,
    )

    student_email = models.EmailField(
        blank=True,
    )

    house = models.CharField(
        max_length=100,
        blank=True,
    )

    boarding_status = models.CharField(
        max_length=50,
        blank=True,
    )

    transport_route = models.CharField(
        max_length=150,
        blank=True,
    )

    club = models.CharField(
        max_length=150,
        blank=True,
    )

    society = models.CharField(
        max_length=150,
        blank=True,
    )

    confidential_notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} Profile"


class Guardian(models.Model):
    full_name = models.CharField(max_length=200)

    relationship = models.CharField(
        max_length=100,
        help_text="Examples: Father, Mother, Uncle, Aunt, Guardian",
    )

    occupation = models.CharField(
        max_length=200,
        blank=True,
    )

    employer = models.CharField(
        max_length=200,
        blank=True,
    )

    phone_number = models.CharField(max_length=30)

    alternative_phone = models.CharField(
        max_length=30,
        blank=True,
    )

    email = models.EmailField(blank=True)

    residential_address = models.TextField(blank=True)

    emergency_contact = models.BooleanField(default=False)

    can_pick_up_student = models.BooleanField(default=True)

    financially_responsible = models.BooleanField(default=False)

    sms_notifications = models.BooleanField(default=True)

    email_notifications = models.BooleanField(default=False)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.relationship})"


class StudentGuardian(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="guardians",
    )

    guardian = models.ForeignKey(
        Guardian,
        on_delete=models.CASCADE,
        related_name="students",
    )

    is_primary_contact = models.BooleanField(
        default=False,
    )

    is_financial_contact = models.BooleanField(
        default=False,
    )

    is_emergency_contact = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "guardian"],
                name="unique_student_guardian",
            )
        ]

    def __str__(self):
        return f"{self.student} ←→ {self.guardian}"


class StudentMedicalProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="medical_profile",
    )

    blood_group = models.CharField(
        max_length=10,
        blank=True,
    )

    genotype = models.CharField(
        max_length=10,
        blank=True,
    )

    allergies = models.TextField(
        blank=True,
    )

    medical_conditions = models.TextField(
        blank=True,
    )

    medications = models.TextField(
        blank=True,
    )

    disabilities = models.TextField(
        blank=True,
    )

    hospital = models.CharField(
        max_length=200,
        blank=True,
    )

    doctor_name = models.CharField(
        max_length=200,
        blank=True,
    )

    doctor_phone = models.CharField(
        max_length=30,
        blank=True,
    )

    emergency_medical_notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} Medical Profile"


class DocumentType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    required_for_admission = models.BooleanField(
        default=False,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class StudentDocument(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        related_name="student_documents",
    )

    title = models.CharField(
        max_length=200,
    )

    file = models.FileField(
        upload_to="students/documents/",
    )

    remarks = models.TextField(
        blank=True,
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.student} - {self.title}"


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
        ordering = [
            "-date_joined",
            "student__first_name",
            "student__other_names",
        ]
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
        ordering = ['student_enrollment__student__first_name', 'student_enrollment__student__other_names', 'class_subject__subject__name']
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
        full_name = " ".join(
            part for part in [self.first_name, self.other_names] if part
        )
        return f"{full_name} ({self.admission_number})"

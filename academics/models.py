from django.db import models


class AcademicSession(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', 'name']

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name='terms',
    )
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['session__start_date', 'start_date', 'name']
        constraints = [
            models.UniqueConstraint(fields=['session', 'name'], name='unique_session_term')
        ]

    def __str__(self):
        return f"{self.session.name} – {self.name}"


class SchoolClass(models.Model):
    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name='classes',
    )
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['session__start_date', 'name']
        constraints = [
            models.UniqueConstraint(fields=['session', 'name'], name='unique_session_class')
        ]

    def __str__(self):
        if self.year:
            return f"{self.session.name} – {self.name} ({self.year})"
        return f"{self.session.name} – {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    # Subject codes are optional for schools that choose to use them.
    # If code uniqueness is needed later, it can be enforced without affecting
    # schools that do not use codes.
    code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self.code:
            return f"{self.name} ({self.code})"
        return self.name


class ClassSubject(models.Model):
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name='class_subjects',
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='class_subjects',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['school_class', 'subject']
        constraints = [
            models.UniqueConstraint(fields=['school_class', 'subject'], name='unique_class_subject')
        ]

    def __str__(self):
        return f"{self.subject} for {self.school_class}"

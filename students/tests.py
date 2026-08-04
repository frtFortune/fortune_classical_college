from django.core.exceptions import ValidationError
from django.test import TestCase

from academics.models import AcademicSession, ClassSubject, SchoolClass, Subject
from students.models import Student, StudentEnrollment, StudentSubject


class EnrollmentAndSubjectValidationTests(TestCase):
    def setUp(self):
        self.session = AcademicSession.objects.create(name='2024/2025', is_active=True)
        self.other_session = AcademicSession.objects.create(name='2025/2026', is_active=False)
        self.school_class = SchoolClass.objects.create(session=self.session, name='JSS 1')
        self.other_class = SchoolClass.objects.create(session=self.other_session, name='JSS 2')
        self.subject = Subject.objects.create(name='English')
        self.class_subject = ClassSubject.objects.create(school_class=self.school_class, subject=self.subject)
        self.other_class_subject = ClassSubject.objects.create(school_class=self.other_class, subject=Subject.objects.create(name='Mathematics'))
        self.student = Student.objects.create(first_name='Ada', last_name='Lovelace', admission_number='ADM-001')

    def test_enrollment_clean_rejects_mismatched_session_and_class(self):
        enrollment = StudentEnrollment(
            student=self.student,
            session=self.session,
            school_class=self.other_class,
        )

        with self.assertRaises(ValidationError):
            enrollment.clean()

    def test_studentsubject_clean_rejects_classsubject_from_different_class(self):
        enrollment = StudentEnrollment.objects.create(
            student=self.student,
            session=self.session,
            school_class=self.school_class,
        )
        student_subject = StudentSubject(
            student_enrollment=enrollment,
            class_subject=self.other_class_subject,
        )

        with self.assertRaises(ValidationError):
            student_subject.clean()

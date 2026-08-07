from django.contrib import admin
from .models import Student, StudentEnrollment, StudentSubject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'other_names', 'admission_number', 'user', 'class_group')
    list_filter = ('class_group',)
    search_fields = ('first_name', 'other_names', 'admission_number', 'user__username')
    ordering = ('other_names', 'first_name')


@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'school_class', 'status', 'date_joined', 'date_left')
    list_filter = ('status', 'session', 'school_class')
    search_fields = ('student__first_name', 'student__other_names', 'student__admission_number', 'session__name', 'school_class__name')
    ordering = ('-date_joined', 'student__other_names', 'student__first_name')


@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    # StudentSubject is an internal data model.
    # Future administrators will assign subjects through bulk spreadsheet-like interfaces rather than editing this model one record at a time.
    list_display = ('student_enrollment', 'class_subject', 'created_at', 'updated_at')
    list_filter = ('student_enrollment__session', 'student_enrollment__school_class', 'class_subject__subject')
    search_fields = ('student_enrollment__student__first_name', 'student_enrollment__student__other_names', 'class_subject__subject__name', 'class_subject__subject__code')
    ordering = ('student_enrollment__student__other_names', 'student_enrollment__student__first_name', 'class_subject__subject__name')

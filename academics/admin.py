from django.contrib import admin
from .models import AcademicSession, AcademicTerm, SchoolClass, Subject, ClassSubject


class AcademicTermInline(admin.TabularInline):
    model = AcademicTerm
    extra = 1


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('-start_date', 'name')
    inlines = [AcademicTermInline]


@admin.register(AcademicTerm)
class AcademicTermAdmin(admin.ModelAdmin):
    list_display = ('name', 'session', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('session',)
    search_fields = ('name', 'session__name')
    ordering = ('session__start_date', 'start_date', 'name')


class ClassSubjectInline(admin.TabularInline):
    model = ClassSubject
    extra = 1


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'session', 'year', 'is_active')
    list_filter = ('session', 'is_active')
    search_fields = ('name', 'session__name')
    ordering = ('session__start_date', 'name')
    inlines = [ClassSubjectInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'subject', 'created_at', 'updated_at')
    list_filter = ('school_class__session', 'subject')
    search_fields = ('school_class__name', 'subject__name', 'subject__code')
    ordering = ('school_class__session__start_date', 'school_class__name', 'subject__name')

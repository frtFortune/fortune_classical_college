from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'admission_number', 'user', 'class_group')
    list_filter = ('class_group',)
    search_fields = ('first_name', 'last_name', 'admission_number', 'user__username')
    ordering = ('last_name', 'first_name')

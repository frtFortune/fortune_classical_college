from django.contrib import admin
from .models import Student, Class, AcademicTerm

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(AcademicTerm)

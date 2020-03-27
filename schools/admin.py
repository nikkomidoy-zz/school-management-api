from django.contrib import admin

from schools.models import School
from students.models import Student


class StudentInline(admin.TabularInline):
    readonly_fields = ('student_id',)
    model = Student
    extra = 1


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]

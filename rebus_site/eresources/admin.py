from eresources.models import Course
from eresources.models import School
from eresources.models import Lecturer
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'school', 'lecturer', 'level', 'language')

admin.site.register(Course, CourseAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'school_url', 'city', 'country')

admin.site.register(School, SchoolAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Lecturer, LecturerAdmin)

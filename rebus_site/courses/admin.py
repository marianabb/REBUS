from courses.models import Course
from courses.models import School
from courses.models import Lecturer
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'lecturer', 'level', 'language')

admin.site.register(Course, CourseAdmin)


# Add 3 courses inline when creating a new School
class CourseInline(admin.StackedInline):
    model = Course
    extra = 3

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'city', 'country')
    inlines = [CourseInline]

admin.site.register(School, SchoolAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Lecturer, LecturerAdmin)

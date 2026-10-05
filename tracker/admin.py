from django.contrib import admin
from.models import Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_dsiplay = ('name','progress')

# Register your models here.

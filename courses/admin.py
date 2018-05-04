from django.contrib import admin

from .models import Course, Step

# Creates inline
class StepInLine(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInLine,]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)

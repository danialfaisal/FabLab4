from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Instructor

class InstructorAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Instructor, InstructorAdmin)

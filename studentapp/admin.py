from django.contrib import admin
from .models import students
# Register your models here.
class studentsadmin(admin.ModelAdmin):
    list_display = ['name','rollno','college']
admin.site.register(students,studentsadmin)
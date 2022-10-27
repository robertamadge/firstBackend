from msilib.schema import Class
from django.contrib import admin
from educations.models import Student, Class

# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
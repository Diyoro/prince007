from django.contrib import admin

# Register your models here.
from .models import AdmitForm, AddTeacher

admin.site.register(AddTeacher)
admin.site.register(AdmitForm)

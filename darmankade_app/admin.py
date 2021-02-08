from django.contrib import admin
from .models import Doctor, Patient, Comment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Comment)

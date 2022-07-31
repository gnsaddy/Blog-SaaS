from django.contrib import admin
from .models import CustomUser, FacultyUserModel

admin.site.register(CustomUser)
admin.site.register(FacultyUserModel)

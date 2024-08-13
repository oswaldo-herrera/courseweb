from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import User

# Register your models here.

admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)

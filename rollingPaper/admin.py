from django.contrib import admin
from .models import RollingInfo
from .models import Comment

admin.site.register(RollingInfo)
admin.site.register(Comment)
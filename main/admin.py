from django.contrib import admin

# Register your models here.

from models import News
admin.site.register(News)

from UserTab.models import UserProfile
admin.site.register(UserProfile)
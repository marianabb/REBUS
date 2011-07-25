from profilemgr.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    pass
    #list_display = ('user.first_name', 'user.last_name', 'user.email')

admin.site.register(UserProfile, UserProfileAdmin)

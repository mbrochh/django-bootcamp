from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', ] 
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    
    
admin.site.register(models.UserProfile, UserProfileAdmin)
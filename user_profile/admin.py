from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
admin.site.register(UserProfile, UserProfileAdmin )


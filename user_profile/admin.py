from django.contrib import admin
from .models import UserProfile, Mentor
from.forms import MentorForm
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
admin.site.register(UserProfile, UserProfileAdmin )

class MentorAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','mentee')
    search_fields = ['mentee', 'mentor']
    form = MentorForm

    fieldsets = (
        (None,{'fields': ('mentor_name', 'mentee_name'),
               }),
    )

    def save_model(self, request, obj, form, change):
        super(MentorAdmin, self).save_model(request, obj, form, change)
admin.site.register(Mentor, MentorAdmin )
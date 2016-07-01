from django.contrib import admin
from .models import Reports
# Register your models here.
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('report_title',)
    search_fields = ['report_title','created_by']

admin.site.register(Reports, ReportsAdmin )
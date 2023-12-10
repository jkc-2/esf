from django.contrib import admin

from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by_email')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by_email')

admin.site.register(Project, ProjectAdmin)

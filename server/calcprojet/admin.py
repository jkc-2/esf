from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


from .models import (
    User,
    Project,
    NeedRessource,
    NeedType,
    Need,
    NeedValue,
    MaterialType,
    MaterialCustomField,
    MaterialCustomFieldValue,
    )


admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(Project, ProjectAdmin)
class NeedRessourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(NeedRessource, NeedRessourceAdmin)

class NeedTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(NeedType, NeedTypeAdmin)

class NeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(Need, NeedAdmin)

class NeedValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'hour_start', 'hour_end', 'day_start', 'day_end', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('value', 'hour_start', 'hour_end', 'day_start', 'day_end', 'created_by')


admin.site.register(NeedValue, NeedValueAdmin)

class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(MaterialType, MaterialTypeAdmin)

class MaterialCustomFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'created_by')

admin.site.register(MaterialCustomField, MaterialCustomFieldAdmin)

class MaterialCustomFieldValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('value', 'created_by')

admin.site.register(MaterialCustomFieldValue, MaterialCustomFieldValueAdmin)
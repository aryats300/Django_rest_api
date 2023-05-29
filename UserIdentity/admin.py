from django.contrib import admin
from .models import UserRole,AssignRole

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'description')

@admin.register(AssignRole)
class AssignRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
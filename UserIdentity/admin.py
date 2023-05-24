from django.contrib import admin
from .models import UserRole

@admin.register(UserRole)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'description')

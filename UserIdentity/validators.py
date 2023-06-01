from rest_framework import serializers
from .models import UserRole

def validate_user_role(attrs):
    role_id = attrs.get('role_id')
    role_name = attrs.get('role_name')
    description = attrs.get('description')

    if UserRole.objects.filter(role_id=role_id).exists():
        raise serializers.ValidationError('Role ID already exists.')

    if UserRole.objects.filter(role_name=role_name).exists():
        raise serializers.ValidationError('Role name already exists.')

    if UserRole.objects.filter(description=description).exists():
        raise serializers.ValidationError('Role description already exists.')

    return attrs

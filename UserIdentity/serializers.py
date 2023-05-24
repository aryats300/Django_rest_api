from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserRole

User=get_user_model()

class UserRegister(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['username','password','email','password2']


    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

        
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserRole
        fields = ['role_id', 'role_name', 'description']
    def validate(self, attrs):
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



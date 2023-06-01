from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from .serializers import UserRoleSerializer
from .models import UserRole
from rest_framework.permissions import IsAuthenticated
from .validators import validate_user_role
from .responses import success_response, error_response


class UserRoleAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = validate_user_role(serializer.validated_data)
            serializer.save()
            return success_response(serializer.data)
        return error_response(serializer.errors, status=400)


class UserRoleDetailsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, role_id):
        try:
            return UserRole.objects.get(role_id=role_id)
        except UserRole.DoesNotExist:
            raise Http404("User role does not exist.")

    def get(self, request, role_id, format=None):
        user_profile = self.get_object(role_id)
        serializer = UserRoleSerializer(user_profile)
        return success_response(serializer.data)

    def put(self, request, role_id, format=None):
        user_role = self.get_object(role_id)
        serializer = UserRoleSerializer(user_role, data=request.data)
        if serializer.is_valid():
            validated_data = validate_user_role(serializer.validated_data)
            serializer.save()
            return success_response(serializer.data)
        return error_response(serializer.errors)

    def delete(self, request, role_id, format=None):
        user_role = self.get_object(role_id)
        user_role.delete()
        return success_response({"message": "User role deleted."})

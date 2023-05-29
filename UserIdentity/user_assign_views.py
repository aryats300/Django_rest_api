from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from .models import UserRole,AssignRole
from .serializers import UserRoleSerializer
from rest_framework.permissions import IsAuthenticated


class AssignUserRoleAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User does not exist.")

        role_id = request.data.get('role_id')
        try:
            role = UserRole.objects.get(role_id=role_id)
        except UserRole.DoesNotExist:
            raise Http404("Role does not exist.")

        assign_role, created = AssignRole.objects.get_or_create(user=user)
        assign_role.role = role
        assign_role.save()

        response_data = {
            "user_id": pk,
            "username": user.username,
            "role": role.role_name
        }

        return Response(response_data)

class UserRolesAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message": "User not found."}, status=404)

        roles = AssignRole.objects.filter(user=user)
        response_data = {
            "user_id": user.pk,
            "username": user.username,
            "roles": [assign_role.role.role_name for assign_role in roles]
        }
        
        return Response(response_data)

# class UserRolesAPI(APIView):
#     def get(self, request, pk, format=None):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({"message": "User not found."}, status=404)

#         roles = AssignRole.objects.filter(user=user)
#         serializer = UserRoleSerializer(roles, many=True)
#         return Response(serializer.data)
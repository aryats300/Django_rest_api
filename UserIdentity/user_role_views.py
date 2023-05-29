
from django.shortcuts import render
from .serializers import UserRoleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import UserRole
from rest_framework.permissions import IsAuthenticated


class UserRoleAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": 'error', 'error': serializer.errors})


class UserRoleDetailsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, role_id):
        try:
            return UserRole.objects.get(role_id=role_id)
        except UserRole.DoesNotExist:
            raise Http404("User profile does not exist.")

    def get(self, request, role_id, format=None):
        user_profile = self.get_object(role_id)
        serializer = UserRoleSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, role_id, format=None):
        user_role = self.get_object(role_id)
        serializer = UserRoleSerializer(user_role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":'error','error':serializer.errors})
        
        # try:
        #     user_role = UserRole.objects.get(role_id=role_id)
        # except UserRole.DoesNotExist:
        #     return Response({"message": "User role not found."}, status=404)

        # serializer = UserRoleSerializer(user_role, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response({"message": "Error", "errors": serializer.errors}, status=400)

    def delete(self, request, role_id, format=None):
        user_profile = self.get_object(role_id)
        user_profile.delete()
        return Response({"message": "User profile deleted."})

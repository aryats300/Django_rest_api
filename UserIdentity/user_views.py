from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, UserDataSerializer
from .responses import success_response, error_response
from .common_views import get, post, put, delete

# class UserAPIView(APIView):
#     def post(self, request, format=None):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             account = serializer.save()
#             data = {
#                 'response': 'registered',
#                 'username': account.username,
#                 'email': account.email,
#             }
#             refresh = RefreshToken.for_user(user=account)
#             data['accesstoken'] = str(refresh.access_token)
#             data['refreshtoken'] = str(refresh)
#             return success_response(data)
#         else:
#             return error_response(serializer.errors)

# class WelcomeAPIView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request):
#         content = {'user': str(request.user), 'userid': str(request.user.id)}
#         return success_response(content)

# class UserDetailsAPIView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404  

#     def get(self, request, pk, format=None):
#         user_data = self.get_object(pk)
#         serializer = UserDataSerializer(user_data)
#         return success_response(serializer.data)

#     def put(self, request, pk, format=None):
#         user_data = self.get_object(pk)
#         serializer = UserDataSerializer(user_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return success_response(serializer.data)
#         else:
#             return error_response(serializer.errors)

#     def delete(self, request, pk, format=None):
#         user_data = self.get_object(pk)
#         user_data.is_deleted = True
#         user_data.save()
#         return success_response({'message': "user soft deleted"})



# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from .serializers import UserRegisterSerializer, UserDataSerializer
# from .common_views import get, post, put, delete

class UserAPIView(APIView):
    def post(self, request, format=None):
        return post(request, UserRegisterSerializer)

class UserDetailsAPIView(APIView):
    def get(self, request, pk, format=None):
        return get(request, User, UserDataSerializer, pk=pk)

    def put(self, request, pk, format=None):
        return put(request, User, UserDataSerializer, pk=pk)

    def delete(self, request, pk, format=None):
        return delete(request, User, pk=pk)


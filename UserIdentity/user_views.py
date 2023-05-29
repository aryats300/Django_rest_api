
from django.shortcuts import render
from .serializers import UserRegister, UserDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserRegister(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registered'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(user=account)
            data['accesstoken'] = refresh.access_token
            data['refreshtoken'] = refresh.refresh_token

        else:
            data = serializer.errors
        return Response(data)


class WelcomeAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {'user': str(request.user), 'userid': str(request.user.id)}
        return Response(content)


class UserDetailsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_data = self.get_object(pk)
        serializer = UserDataSerializer(user_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_data = self.get_object(pk)
        serializer = UserDataSerializer(user_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": 'error', 'error': serializer.errors})

    def delete(self, request, pk, format=None):
        user_data = self.get_object(pk)
        user_data.is_deleted = True
        user_data.save()
        return Response({'message': "user soft deleted"})


# class UserAuthenticationAPI(APIView):
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         # Assuming you have a User model
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#             refresh_token = str(refresh)

#             return Response({'access_token': access_token, 'refresh_token': refresh_token})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=401)

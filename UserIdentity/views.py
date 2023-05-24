from django.shortcuts import render
from .serializers import UserRegister,UserDataSerializer,UserRoleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from .models import UserRole

# Create your views here.
class user(APIView):
     def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data) 

class welcome(APIView):
    permission_classes= (IsAuthenticated,)
    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)
    
class userDetails(APIView): 
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404
                
    def get(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":'error','error':serializer.errors}) 
    
 
    def delete(self, request, pk, format=None):
        userData = self.get_object(pk)
        userData.is_deleted = True
        userData.save()
        return Response({'message': "user soft deleted"})
    
    

class user_role(APIView):
    def post(self, request, format=None):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":'error','error':serializer.errors})
    
class user_role_Details(APIView):
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
    
    def delete(self, request, role_id, format=None):
        user_profile = self.get_object(role_id)
        user_profile.delete()
        return Response({"message": "User profile deleted."})




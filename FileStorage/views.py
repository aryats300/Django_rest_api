from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadSerializer

# Create your views here.
class UploadAPIView(APIView):
    def post(self, request, format=None):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response(serializer.errors)
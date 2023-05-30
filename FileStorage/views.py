from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadSerializer

# Create your views here.
class UploadAPIView(APIView):
    def post(self, request, format=None):
        allowed_types = ['image/jpeg', 'image/png']
        serializer = UploadSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['file'].content_type not in allowed_types:
                return Response("Only JPG and PNG files are allowed.", status=400)

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)




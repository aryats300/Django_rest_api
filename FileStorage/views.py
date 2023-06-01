from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UploadSerializer
from .models import Upload
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .response import success_response, error_response, download_response


class UploadAPIView(APIView):
    def post(self, request, format=None):
        allowed_types = ['image/jpeg', 'image/png']
        serializer = UploadSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['file'].content_type not in allowed_types:
                return error_response("Only JPG and PNG files are allowed.", status=400)

            serializer.save()
            return success_response(serializer.data)

        return error_response(serializer.errors, status=400)


class DownloadAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, file_id, format=None):
        upload = get_object_or_404(Upload, file_id=file_id)
        return download_response(upload.file, content_type='image/jpeg', filename=upload.file.name)

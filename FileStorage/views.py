from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadSerializer
from .models import Upload
from rest_framework.permissions import IsAuthenticated
# from django.urls import reverse

from django.shortcuts import get_object_or_404

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

class DownloadAPIView(APIView):

    # permission_classes = (IsAuthenticated,)
    def get(self, request, file_id, format=None):
        upload = get_object_or_404(Upload, file_id=file_id)
        response = HttpResponse(upload.file, content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{upload.file.name}"'
        return response

        # def get(self, request, file_id, format=None):
        #     upload = get_object_or_404(Upload, file_id=file_id)

        #     download_url = reverse('Download', args=[file_id])
        #     response_data = {
        #         'file_name': upload.file.name,
        #         'download_url': request.build_absolute_uri(download_url),
        #     }

        #     return Response(response_data)
        
        




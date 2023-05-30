from django.urls import path
from .views import UploadAPIView,DownloadAPIView

urlpatterns = [
path('fileupload/', UploadAPIView.as_view(), name='Upload'),
path('filedownload/<int:file_id>/', DownloadAPIView.as_view(), name='Upload'),

]
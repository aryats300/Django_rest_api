from django.urls import path
from .views import UploadAPIView

urlpatterns = [
path('fileupload/', UploadAPIView.as_view(), name='Upload'),


]
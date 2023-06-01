from django.http import HttpResponse
from rest_framework.response import Response


def success_response(data=None):
    return Response(data)


def error_response(errors, status=400):
    return Response(errors, status=status)


def download_response(file, content_type, filename):
    response = HttpResponse(file, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

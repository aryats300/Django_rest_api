from rest_framework.response import Response

def success_response(data=None):
    return Response(data)

def error_response(errors, status=400):
    return Response({"message": 'error', 'error': errors}, status=status)

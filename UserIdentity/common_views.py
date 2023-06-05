from rest_framework.response import Response
from django.http import Http404

def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404("Object does not exist.")

def get(request, model, serializer_class, **kwargs):
    obj = get_object_or_404(model, **kwargs)
    serializer = serializer_class(obj)
    return Response(serializer.data)

def post(request, serializer_class):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

def put(request, model, serializer_class, **kwargs):
    obj = get_object_or_404(model, **kwargs)
    serializer = serializer_class(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

def delete(request, model, **kwargs):
    obj = get_object_or_404(model, **kwargs)
    obj.delete()
    return Response({"message": "Object deleted."})

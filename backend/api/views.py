from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import *
# Create your views here.
@api_view(['GET'])
def overview(request):
    context = {
        'list':'/list',
        'detail':'/detail',
        'create':'/create',
        'update':'/update',
        'delete':'/delete',        
    }
    return Response(context)

@api_view(['GET'])
def list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response()    

def token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})
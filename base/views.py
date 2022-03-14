from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    return Response('Hello world')

@api_view(['POST'])
def getPost(request):
    print('request data:',request.data)
    return Response('Hello world')

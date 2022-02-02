from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import (about_us,news,full,partial,bachalor,masters,phd)
from .serializer import (about__us,news_serial,full_serial,partial_serial,bachalor_serial,masters_serial,phd_serial)


@api_view(['GET'])
def us(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = about_us.objects.all()
        serializers = about__us(snippets, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def newss(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = news.objects.all()
        serializers = news_serial(snippets, many=True)
        return Response(serializers.data)    


@api_view(['GET'])
def full_scholar(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = full.objects.all()
        serializers = full_serial(snippets, many=True)
        return Response(serializers.data)  

@api_view(['GET'])
def partial_scholar(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = partial.objects.all()
        serializers = partial_serial(snippets, many=True)
        return Response(serializers.data) 


@api_view(['GET'])
def bac_view(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = bachalor.objects.all()
        serializers = bachalor_serial(snippets, many=True)
        return Response(serializers.data)      

@api_view(['GET'])
def mas_view(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = masters.objects.all()
        serializers = masters_serial(snippets, many=True)
        return Response(serializers.data) 

@api_view(['GET'])
def phd_view(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = phd.objects.all()
        serializers = phd_serial(snippets, many=True)
        return Response(serializers.data)                                                                                                      
from django.shortcuts import render
from APIRest.serializers import NoticiaSerializer
from rest_framework import generics

from core.models import Noticia

class NoticiaList(generics.ListCreateAPIView):
	queryset = Noticia.objects.all()
	serializer_class = NoticiaSerializer

# class NoticiaDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Noticia.objects.all()
# 	serializer_class = NoticiaSerializer
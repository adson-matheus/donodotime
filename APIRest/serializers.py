from rest_framework import serializers
from core.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Noticia
		fields = ['id', 'titulo', 'autor', 'data',]
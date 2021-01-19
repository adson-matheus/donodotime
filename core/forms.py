from django import forms
from .models import Noticia, Comentario

class noticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ['titulo', 'reportagem_pt1', 'reportagem_pt2', 'autor', 'tweet', 'url_foto', 'autorais_foto',]

class editarNoticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ['titulo', 'reportagem_pt1', 'reportagem_pt2', 'tweet', 'url_foto', 'autorais_foto',]

class comentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['noticia', 'nome', 'comment',]
from django.db import models

class Noticia(models.Model):
	titulo = models.CharField(max_length=255, blank=False)
	reportagem_pt1 = models.TextField(max_length=800, blank=False)
	reportagem_pt2 = models.TextField(max_length=800, blank=True)
	autor = models.CharField(max_length=50, blank=True)
	tweet = models.TextField(max_length=800, blank=True)
	url_foto = models.TextField(max_length=800, blank=True)
	autorais_foto = models.CharField(max_length=100, blank=True)
	data = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ('-id',)
	def __str__(self):
		return self.titulo


class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, related_name='comentarios', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50, blank=False, null=False)
	comment = models.TextField(max_length=255, blank=False, null=False)
	data = models.DateField(auto_now_add=True)

	def __str__(self):
		return '%s, por: %s' %(self.noticia.titulo, self.nome)
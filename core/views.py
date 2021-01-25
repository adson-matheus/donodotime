from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import noticiaForm, comentarioForm, editarNoticiaForm
from .models import Noticia, Comentario

def index(request):
	noticia = Noticia.objects.all()
	if len(noticia) >= 4:
		#traz os 3 ultimos resultados, excluindo o primeiro
		last_news = noticia[1:4]
	elif len(noticia) >= 3:
		last_news = noticia[1:3]
	elif len(noticia) >= 2:
		last_news = noticia[1:2]
	else:
		last_news = None

	#verifica se há noticias cadastradas e
	#pega a primeira noticia para a parte principal
	if len(noticia) > 0:
		noticia = noticia[0]
	else:
		noticia = None
	return render(request, 'core/index.html', {'noticia': noticia, 'last_news':last_news})

class noticiaListView(generic.ListView):
	model = Noticia

def noticiaDetalhe(request, id):
	noticia = Noticia.objects.get(pk=id)
	#qte. de comentarios
	q = noticia.comentarios
	qte = q.count()
	return render(request, 'core/noticia_detail.html', {'noticia':noticia, 'qte':qte})

#forms
@login_required
def noticiaCadastro(request):
	if not request.user.is_staff:
		return redirect('core:index')
	else:
		if request.method == 'POST':
			form = noticiaForm(request.POST)
			if form.is_valid:
				form.save()
				return redirect('core:noticiaListView')
		else:
			form = noticiaForm()
	return render(request, "core/noticia_cadastro.html", {'form':form})

@login_required
def noticiaEdit(request, id):
	if not request.user.is_staff:
		return redirect('core:index')
	else:
		form_id = Noticia.objects.get(pk=id)
		if request.method == 'POST':
			form = editarNoticiaForm(request.POST, instance=form_id)
			if form.is_valid():
				form.save()
				return redirect('core:noticiaDetalhe', form_id.id)
		else:
			form = editarNoticiaForm(instance=form_id)
		return render(request, 'core/noticia_edit.html', {'form':form})

# um botao antes de excluir permanente
@login_required
def noticiaExcluirBotao(request, id):
	if not request.user.is_staff:
		return redirect('core:index')
	else:
		form = Noticia.objects.get(pk=id)
	return render(request, 'core/noticia_delete.html', {'form':form})

# exclusao permanente
@login_required
def noticiaExcluir(request, id):
	if not request.user.is_staff:
		return redirect('core:index')
	else:
		form = Noticia.objects.get(pk=id)
		form.delete()
	return redirect('core:noticiaListView')



@login_required
def comentarioCadastro(request, id):
	id_noticia = Noticia.objects.get(pk=id)
	if not request.user.is_authenticated:
		return render('core:index')
	else:
		if request.method == 'POST':
			form = comentarioForm(request.POST)
			if form.is_valid:
				form.save()
				return redirect('core:noticiaDetalhe', id_noticia.id)
		else:
			form = comentarioForm()
	return render(request, "core/comentario_cadastro.html", {'form':form, 'id_noticia':id_noticia,})
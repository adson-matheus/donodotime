from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import noticiaForm, comentarioForm, editarNoticiaForm
from .models import Noticia

def index(request):
	query = Noticia.objects.all()
	if len(query) > 0:
		query = query[0]
	else:
		return render(request, 'core/index.html')
	return render(request, 'core/index.html', {'query': query})

class noticiaListView(generic.ListView):
	model = Noticia

class noticiaDetailView(generic.DetailView):
	model = Noticia

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
				return redirect('core:noticiaDetailView', form_id.id)
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
				return redirect('core:noticiaDetailView', id_noticia.id)
		else:
			form = comentarioForm()
	return render(request, "core/comentario_cadastro.html", {'form':form, 'id_noticia':id_noticia})

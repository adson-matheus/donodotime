from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
	path('', views.index, name='index'),

	path('noticias/', views.noticiaListView.as_view(), name='noticiaListView'),
	path('noticias/new/', views.noticiaCadastro, name='noticiaCadastro'),
	path('noticias/<int:pk>/', views.noticiaDetailView.as_view(), name='noticiaDetailView'),
	path('noticias/<int:id>/edit/', views.noticiaEdit, name='noticiaEdit'),
	path('noticias/<int:id>/delete/', views.noticiaExcluirBotao, name='noticiaExcluirBotao'),
	path('noticias/<int:id>/delete/confirm/', views.noticiaExcluir, name='noticiaExcluir'),

	path('comentarios/<int:id>/new/', views.comentarioCadastro, name='comentarioCadastro'),
]
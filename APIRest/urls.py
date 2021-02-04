from django.urls import path
from APIRest import views

urlpatterns = [
	# api/
	path('noticias/', views.NoticiaList.as_view()),
#	path('noticias/<int:pk>', views.NoticiaDetail.as_view()),
]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from donodotime import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
    name='logout'),
]

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]

from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView, LoginView
from .views import SobreView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name='NomeDaUrl'),
    path('', IndexView.as_view(), name='inicio'),
    path('sobre', SobreView.as_view(), name='sobre'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
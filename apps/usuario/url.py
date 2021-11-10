from django.contrib.auth.views import LogoutView
from django.urls import path
from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
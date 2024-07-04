from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrar/', views.registrar_usuario),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
]
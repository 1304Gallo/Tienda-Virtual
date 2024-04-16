from django.contrib.auth import views as auth_views
from django.urls import path
from Apps.usuario.views import *

urlpatterns = [

    path('', LoginFormView.as_view(), name='login'),
    path('logout', LogoutRedirectView.as_view(), name='logout'),
    path('crear_usuario/', CreateUserFormView.as_view(), name='crear_usuario'),

]

from django.contrib.auth import views as auth_views
from django.urls import path
from Apps.login.views import *

urlpatterns = [

    path('', LoginFormView.as_view(), name='login'),  
    #path('logout', LogoutView.as_view(), name='logout'),
    path('logout', LogoutRedirectView.as_view(), name='logout'),

]

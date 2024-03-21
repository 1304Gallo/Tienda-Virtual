from django.contrib import admin
from django.urls import path, include
from Apps.login.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('Apps.login.urls')),  
    path('almacen', include('Apps.almacen.urls')),
    path('', include('Apps.store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
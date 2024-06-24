from django.contrib import admin
from django.urls import path, include

from core.views import tienda

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', tienda, name='Tienda'),
]
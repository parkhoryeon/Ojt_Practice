from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls", namespace="core")), 
    path('api/v1/users/', include("users.urls", namespace="users")),
]

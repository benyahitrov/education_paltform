from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('base_app.urls', namespace='base_app')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
]

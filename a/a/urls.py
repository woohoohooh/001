from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
]

# Добавляем обработку статики
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

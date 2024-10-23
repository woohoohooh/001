from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Определение URL-паттернов
urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
]

# Обработка статики и медиа
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавление пути для robots.txt
urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name='data/robots.txt', content_type='text/plain')),
]

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
    # Указываем рабочие прямые ссылки для favicon.ico и robots.txt
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='https://s3.timeweb.cloud/23b150f1-bc6e7174-c901-4463-91a6-db6756f1714d/favicon.ico', permanent=True)),
    re_path(r'^robots\.txt$', RedirectView.as_view(url='https://s3.timeweb.cloud/23b150f1-bc6e7174-c901-4463-91a6-db6756f1714d/robots.txt', permanent=True)),
]

# Остальные настройки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

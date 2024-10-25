from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('q/', admin.site.urls),
    path('', include('data.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=f'{settings.STATIC_URL}favicon.ico', permanent=True)),
    re_path(r'^robots\.txt$', RedirectView.as_view(url=f'{settings.STATIC_URL}robots.txt', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

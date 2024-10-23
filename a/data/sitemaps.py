from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Company, Rubrics

# Sitemap для рубрик
class RubricsSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения рубрик
    priority = 0.6  # Приоритет страницы

    def items(self):
        return Rubrics.objects.filter(visible=True)  # Отображаем только видимые рубрики

    def location(self, obj):
        return reverse('rubric_detail', args=[obj.slug])  # Используем slug для URL

# Sitemap для компаний
class CompanySitemap(Sitemap):
    changefreq = 'daily'  # Частота изменения страницы
    priority = 0.8  # Приоритет страницы

    def items(self):
        return Company.objects.filter(visible=True)  # Отображаем только видимые компании

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, 'updated_at') else None

    def location(self, obj):
        return reverse('company_detail', args=[obj.slug])  # Используем slug для URL

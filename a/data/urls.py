from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import RubricsSitemap, CompanySitemap
from .views import (
    index, forstart, delete_company, company_detail, rubric_detail,
    add_comment, company_detail2_2, start, test, test2,
    start_add_prefixes, start_add_zero_rubric, toggle_visibility
)
from django.conf.urls import handler404
from django.views.generic import TemplateView

sitemaps = {
    'rubrics': RubricsSitemap,
    'companies': CompanySitemap,
}

urlpatterns = [
    path('start/', start, name='start'),  # Стартовая страница
    path('forstart/', forstart, name='forstart'),  # Для начала
    path('', index, name='index'),  # Главная страница
    path('rubrics/<str:slug>/', rubric_detail, name='rubric_detail'),  # Подробности рубрики
    path('test/', test, name='test'),  # Тестовая страница 1
    path('test2/', test2, name='test2'),  # Тестовая страница 2
    path('<str:slug>/', company_detail, name='company_detail'),  # Подробности компании по slug
    path('2/<int:pk>/', company_detail2_2, name='company_detail2_2'),  # Подробности компании по pk
    path('start_add_prefixes/', start_add_prefixes, name='start_add_prefixes'),  # Добавление префиксов
    path('start_add_zero_rubric/', start_add_zero_rubric, name='start_add_zero_rubric'),  # Добавление нулевой рубрики
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),  # Добавление комментария к посту
    path('company/<int:pk>/toggle_visibility/', toggle_visibility, name='toggle_visibility'),  # Переключение видимости компании
    path('company/delete/<int:pk>/', delete_company, name='delete_company'),  # Удаление компании
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # Sitemap
]

handler404 = 'data.views.custom_404_view'

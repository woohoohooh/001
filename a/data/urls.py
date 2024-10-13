from django.urls import path
from .views import index, forstart, delete_company, company_detail, rubric_detail, add_comment, company_detail2_2, start, test, test2, start_add_prefixes, start_add_zero_rubric, toggle_visibility

urlpatterns = [
    path('start/', start, name='start'),
    path('forstart/', forstart, name='forstart'),
    path('', index, name='index'),
    path('rubrics/<str:slug>/', rubric_detail, name='rubric_detail'),
    path('test/', test, name='test'),
    path('test2/', test2, name='test2'),
    path('<str:slug>/', company_detail, name='company_detail'),
    path('2/<int:pk>/', company_detail2_2, name='company_detail2_2'),
    path('start_add_prefixes/', start_add_prefixes, name='start_add_prefixes'),
    path('start_add_zero_rubric/', start_add_zero_rubric, name='start_add_zero_rubric'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('company/<int:pk>/toggle_visibility/', toggle_visibility, name='toggle_visibility'),
    path('company/delete/<int:pk>/', delete_company, name='delete_company'),


]

handler404 = 'views.custom_404_view'
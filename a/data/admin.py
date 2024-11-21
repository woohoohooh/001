from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Company, Rubrics
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.urls import path, reverse
from django.utils.html import format_html
from .models import Company, Rubrics, FileTracker

class FileTrackerAdmin(admin.ModelAdmin):
    list_display = ('filename',)  # Замените 'last_filename' на правильное поле

admin.site.register(FileTracker, FileTrackerAdmin)

from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.urls import path, reverse
from django.utils.html import format_html
from .models import Company, Rubrics

class RubricsAdmin(admin.ModelAdmin):
    list_display = ['name_original', 'visible', 'company_count_link']
    list_editable = ['visible']
    search_fields = ['name_original']
    actions = ['make_all_visible', 'make_all_invisible']

    def make_all_visible(self, request, queryset):
        queryset.update(visible=True)
        self.message_user(request, "Все выбранные рубрики теперь видимы.")

    def make_all_invisible(self, request, queryset):
        queryset.update(visible=False)
        self.message_user(request, "Все выбранные рубрики теперь скрыты.")

    make_all_visible.short_description = "Сделать все рубрики видимыми"
    make_all_invisible.short_description = "Сделать все рубрики скрытыми"

    def company_count_link(self, obj):
        count = obj.company_set.count()
        if count == 0:
            return 'No companies'
        url = reverse("admin:%s_%s_changelist" % (obj._meta.app_label, Company._meta.model_name))
        url += f'?rubrics__id__exact={obj.id}'
        return format_html('<a href="{}">{} companies</a>', url, count)

    company_count_link.short_description = "Companies"

class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'org_name1', 'slug', 'mainnew', 'org_name2',
        'ads_article', 'article_warning', 'description',
        'org_name3', 'address_comment'
    ]
    search_fields = ['org_name1', 'mainnew']
    actions = ['delete_all']
    ordering = ['slug']
    filter_horizontal = ['rubrics']

    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Selected items have been deleted.")

    delete_all.short_description = "Delete all selected items"

    # Переопределение метода для поиска объекта по slug
    def get_object(self, request, object_id, from_field=None):
        queryset = self.get_queryset(request)
        model = queryset.model

        # Попытка найти объект по ID
        try:
            return queryset.get(pk=object_id)
        except model.DoesNotExist:
            pass

        # Поиск по slug, если ID не найден
        try:
            return queryset.get(slug=object_id)
        except model.DoesNotExist:
            raise Http404(_("No %(name)s found matching the query") % {
                'name': model._meta.verbose_name
            })

    # Переопределение метода get_urls, чтобы использовать slug в URL
    def get_urls(self):
        from django.urls import path

        urls = super().get_urls()
        custom_urls = [
            path('<slug:object_id>/change/', self.admin_site.admin_view(self.change_view),
                 name=f'{self.model._meta.app_label}_{self.model._meta.model_name}_change_slug'),
        ]

        return custom_urls + urls

# Регистрация моделей в админке
admin.site.register(Rubrics, RubricsAdmin)
admin.site.register(Company, CompanyAdmin)

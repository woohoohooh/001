from django.contrib import admin
from django.urls import reverse
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
        # Use the correct URL name for the Company model's change list view
        url = reverse("admin:%s_%s_changelist" % (obj._meta.app_label, Company._meta.model_name))
        url += f'?rubrics__id__exact={obj.id}'
        return format_html('<myproject href="{}">{} companies</myproject>', url, count)

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
    filter_horizontal = ['rubrics']  # Use this for better selection UI for ManyToManyField

    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Selected items have been deleted.")

    delete_all.short_description = "Delete all selected items"

admin.site.register(Rubrics, RubricsAdmin)
admin.site.register(Company, CompanyAdmin)

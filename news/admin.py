from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published', 'get_image',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ('title', 'content', 'image', 'get_image',
              'view', 'is_published', 'update', 'created_at')
    readonly_fields = ('get_image', 'view', 'update', 'created_at')
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'Фото не установлено'

    get_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управлениe новостями'
admin.site.site_header = 'Управлениe новостями'

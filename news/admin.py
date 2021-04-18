from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                    'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

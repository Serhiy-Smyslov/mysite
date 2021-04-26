from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    """Return all categories on the get_list_categoies page."""
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    """Add attributes in a dict on list_categories template."""
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(
            cnt=Count('news'),
            filter=F('news__is_published')).filter(cnt__gt=0)  # Count amount of news by categories.
        cache.set('categories', categories, 30)
    # categories = Category.objects.all()
    return {'categories': categories}

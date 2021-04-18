from django.shortcuts import render
from .models import News


# Create your views here.
def news(request):
    all_news = News.objects.all()
    return render(request, 'news/news.html', {'all_news': all_news})
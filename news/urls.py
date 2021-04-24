from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('', views.news, name='news'),
    # path('categories/<int:category_id>', views.get_news_by_categories, name='news_by_category'),
    path('categories/<int:category_id>/', views.NewsByCategory.as_view(), name='news_by_category'),
    # path('news/<int:news_id>', views.view_news, name='view_news'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', views.add_news, name='add_news'),
    path('news/add-news/', views.CreateNews.as_view(), name='add_news'),
]

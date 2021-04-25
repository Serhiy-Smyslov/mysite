from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('test/', views.test, name='test'),
    path('send_message/', views.send_message_to_email, name='contact'),
    path('', cache_page(10)(views.HomeNews.as_view()), name='home'),
    # path('', views.news, name='news'),
    # path('categories/<int:category_id>', views.get_news_by_categories, name='news_by_category'),
    path('categories/<int:category_id>/', views.NewsByCategory.as_view(), name='news_by_category'),
    # path('news/<int:news_id>', views.view_news, name='view_news'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', views.add_news, name='add_news'),
    path('news/add-news/', views.CreateNews.as_view(), name='add_news'),
]

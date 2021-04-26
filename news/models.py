from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model in database which safe categories information."""
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')

    def get_absolute_url(self):  # Return template with news by unique category.
        return reverse('news_by_category', kwargs={'category_id': self.pk})

    class Meta:
        """Metadata of class."""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    """Model in database which safe news information."""
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновление')
    image = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')  # Connect categories with news.
    view = models.IntegerField(default=0)

    def get_absolute_url(self):  # Return template with new.
        return reverse('view_news', kwargs={'pk': self.pk})

    class Meta:
        """Metadata of class."""
        verbose_name = 'Новоcть'
        verbose_name_plural = 'Новости'
        ordering = ['title',]

    def __str__(self):
        return self.title

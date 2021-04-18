from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновление')
    image = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Новоcть'
        verbose_name_plural = 'Новости'
        ordering = ['title',]

    def __str__(self):
        return self.title

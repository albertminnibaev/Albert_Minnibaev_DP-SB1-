from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):

    title = models.CharField(max_length=250, unique=True, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='пользователь, который создал объявление', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания объявления')
    image = models.ImageField(upload_to='ad_images/', **NULLABLE, verbose_name='изображение')

    def __str__(self):
        return f'{self.title} {self.price}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ("-created_at",)


class Comment(models.Model):

    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление', related_name='comment', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания отзыва')

    def __str__(self):
        return f'{self.text} {self.author} ({self.ad})'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ("-created_at",)

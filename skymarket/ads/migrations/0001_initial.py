# Generated by Django 5.0 on 2023-12-25 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='название товара')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='цена товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания объявления')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ad_images/', verbose_name='изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь, который создал объявление')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания отзыва')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='ads.ad', verbose_name='объявление')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
                'ordering': ('-created_at',),
            },
        ),
    ]

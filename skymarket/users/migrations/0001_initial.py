# Generated by Django 5.0 on 2023-12-25 19:08

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='адрес электронной почты')),
                ('role', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=10, verbose_name='роль пользователя')),
                ('image', models.ImageField(blank=True, default='users/avatar_default.jpeg', null=True, upload_to='users/', verbose_name='аватар')),
                ('is_active', models.BooleanField(default=True, verbose_name='статус акаунта')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]

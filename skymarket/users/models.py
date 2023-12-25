from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'null': True, 'blank': True}


class User(AbstractBaseUser):

    username = None

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = PhoneNumberField(verbose_name="номер телефона")
    email = models.EmailField(unique=True, verbose_name="адрес электронной почты")
    role = models.CharField(max_length=10, choices=UserRoles.choices,
                            default=UserRoles.USER, verbose_name="роль пользователя")
    image = models.ImageField(upload_to='users/', default='users/avatar_default.jpeg',
                              verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="статус акаунта")

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return f'{self.email}, {self.phone}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

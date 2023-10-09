from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from .validators import validate_username


class CustomUser(AbstractUser):
    """Класс модели пользователя."""

    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        validators=[EmailValidator()],
        error_messages={
            'unique': ('Пользователь с таким email уже существует!'),
        },
        blank=True, null=True
    )
    username = models.CharField(
        'Лента ID',
        max_length=150,
        unique=True,
        validators=(validate_username,)
    )
    password = models.CharField(
        'Пароль',
        max_length=150,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_email_domain, validate_password_strength

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', validators=[validate_email_domain])
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата рождения', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def set_password(self, raw_password):
        validate_password_strength(raw_password)
        super().set_password(raw_password)


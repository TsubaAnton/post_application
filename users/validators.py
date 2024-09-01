import re
from django.core.exceptions import ValidationError


def validate_password_strength(value):
    if len(value) < 8:
        raise ValidationError('Пароль должен быть не менее 8 символов')
    if not re.search(r'\d', value):
        raise ValidationError('Пароль должен содержать цифры')


def validate_email_domain(value):
    valid_domain = ['mail.ru', 'yandex.ru']
    email_domain = value.split('@')[-1]
    if email_domain not in valid_domain:
        raise ValidationError('Домен почты должен быть mail.ru или yandex.ru')

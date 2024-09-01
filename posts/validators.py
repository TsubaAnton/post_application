from django.core.exceptions import ValidationError
from datetime import date


def validate_author_age(author):
    if author.birth_date:
        age = date.today().year - author.birth_date.year
        if age < 18:
            raise ValidationError('Автор поста должен быть старше 18 лет')


def validate_post_title(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    if any(word in value.lower() for word in forbidden_words):
        raise ValidationError('В заголовке используются запрещенные слова')


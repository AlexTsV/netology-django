from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    value = datetime.date(value)
    return value


# необходимо добавить фильтр для поля `score`
@register.filter
def format_date(value):
    # Ваш код
    # return value
    pass


@register.filter
def format_num_comments(value):
    # Ваш код
    return value




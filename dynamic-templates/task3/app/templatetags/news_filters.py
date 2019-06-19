from django import template
import datetime

register = template.Library()


@register.filter
def format_date(value):
    date = datetime.datetime.fromtimestamp(value)
    now = datetime.datetime.now()
    delta = (now - date).seconds / 60
    if delta < 10:
        return 'Только что'
    if delta < 1440:
        return f'{int(delta / 60)} часов назад'
    if delta > 1440:
        return date.strftime('%Y %B %d')


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if value < -5:
        return 'Все плохо'
    if value - 5 <= value <= 5:
        return 'Нейтрально'
    if value > 5:
        return 'Хорошо'
    return value


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставить комментарий'
    if 0 <= value <= 50:
        return f'{value}'
    if value > 50:
        return '50+'


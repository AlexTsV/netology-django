from django import forms
from .widgets import AjaxInputWidget, TextInput
from django.forms.widgets import SelectDateWidget, Select
from .models import City


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    arrival = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs={'class': 'inline right-margin'}),
                              label='Прибытие')
    cities = City.objects.all()
    cities_choice = list()
    for i in enumerate(cities):
        cities_choice.append(i)
    departure = forms.ChoiceField(choices=cities_choice, label='Отправление')
    date = forms.DateField(widget=SelectDateWidget, label='Дата')

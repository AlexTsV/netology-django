from django import forms
from .widgets import AjaxInputWidget, TextInput
from django.forms.widgets import SelectDateWidget
from .models import City


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    arrival = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs={'class': 'inline right-margin'}),
                              label='Прибытие')
    departure = forms.ChoiceField(widget=TextInput, label='Отправление')
    date = forms.DateField(widget=SelectDateWidget, label='Дата')

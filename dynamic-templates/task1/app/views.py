from django.shortcuts import render
import csv
from decimal import Decimal

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    inflation = list()
    with open('inflation_russia.csv', 'r', encoding='utf-8') as file:
        readline = csv.DictReader(file, delimiter=';')
        for line in readline:
                data = {'Year': line['Год'], 'Jan': float(line['Янв']), 'Feb': float(line['Фев']), 'Mar': float(line['Мар']), 'Apr': float(line['Апр']),
                        'May': float(line['Май']), 'Jun': float(line['Июн']), 'Jul': float(line['Июл']), 'Aug': float(line['Авг']), 'Sep': float(line['Сен']),
                        'Oct': float(line['Окт']), 'Nov': float(line['Ноя']), 'Dec': float(line['Дек']), 'Sum': float(line['Суммарная'])}
                inflation.append(data)
    context = {'inflation': inflation}

    return render(request, template_name,
                  context)
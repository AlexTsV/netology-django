from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    inflation = list()
    with open('inflation_russia.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for line in reader:
            data = {'Year': line['Год'],
                    'Jan': float(line['Янв']) if line['Янв'] != '' else line['Янв'],
                    'Feb': float(line['Фев']),
                    'Mar': float(line['Мар']),
                    'Apr': float(line['Апр']),
                    'May': float(line['Май']),
                    'Jun': float(line['Июн']),
                    'Jul': float(line['Июл']),
                    'Aug': float(line['Авг']),
                    'Sep': float(line['Сен']) if line['Сен'] != '' else line['Сен'],
                    'Oct': float(line['Окт']) if line['Окт'] != '' else line['Окт'],
                    'Nov': float(line['Ноя']) if line['Ноя'] != '' else line['Ноя'],
                    'Dec': float(line['Дек']) if line['Дек'] != '' else line['Дек'],
                    'Sum': float(line['Суммарная'])}
            inflation.append(data)
    context = {'inflation': inflation}

    return render(request, template_name,
                  context)

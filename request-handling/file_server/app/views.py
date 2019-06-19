import datetime
from django.conf import settings
from django.shortcuts import render
import os
from django.http import Http404


def file_list(request, date=None):
    template_name = 'index.html'

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = os.listdir(settings.FILES_PATH)
    context = {
        'files': [

        ],
    }
    if date:
        context['date'] = date.date()  # Этот параметр необязательный
    for file in files:
        file_stat = os.stat(f'{settings.FILES_PATH}/{file}')
        file_stat_dict = {'name': file, 'ctime': datetime.datetime.fromtimestamp(file_stat.st_ctime),
                          'mtime': datetime.datetime.fromtimestamp(file_stat.st_ctime)}
        context['files'].append(file_stat_dict)

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    try:
        with open(os.path.join(settings.FILES_PATH, name), encoding='utf-8') as file:
            file_data = file.read()
    except FileNotFoundError:
        raise Http404
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_data}
    )

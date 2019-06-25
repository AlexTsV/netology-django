import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
import re

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    search_city = request.GET.get('term')
    cities = City.objects.all()
    result = list()
    for city in cities:
        result.append(city.name)
    r = re.compile(f"(?i){search_city}")
    new_result = list(filter(r.match, result))
    return JsonResponse(new_result, safe=False)

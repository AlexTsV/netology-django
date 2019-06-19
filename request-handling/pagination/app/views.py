import urllib.parse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request, page=None):
    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=',')
        bus_stations = list()
        for row in reader:
            station = {'Name': row['StationName'], 'Street': row['Street'], 'District': row['District']}
            bus_stations.append(station)

    page = request.GET.get('page')
    paginator = Paginator(bus_stations, 10)
    current_page = paginator.get_page(page)
    if page:
        return render_to_response('index.html', context={
            'bus_stations': paginator.page(page),
            'current_page': page,
            'prev_page_url': '?' + urllib.parse.urlencode(
                {'page': current_page.previous_page_number()}) if current_page.has_previous() else None,
            'next_page_url': '?' + urllib.parse.urlencode(
                {'page': current_page.next_page_number()}) if current_page.has_next() else None
        })

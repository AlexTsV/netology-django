from django.shortcuts import render
from .models import Phone, Samsung, Apple, Xiaomi


def show_catalog(request):
    phones = Phone.objects.all()
    print(phones)
    optionals = list()
    samsung = Samsung.objects.all()
    optionals.append(samsung)
    apple = Apple.objects.all()
    optionals.append(apple)
    xiaomi = Xiaomi.objects.all()
    optionals.append(xiaomi)
    template = 'catalog.html'
    context = {'phones': phones,
               'optionals': optionals}
    return render(
        request,
        template,
        context
    )

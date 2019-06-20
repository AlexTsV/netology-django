from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
<<<<<<< HEAD
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    name = request.GET.get('name')
    if sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    if sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    if name:
        phones = Phone.objects.all().order_by('name')
    context = {'phones': phones}
=======
    context = {}
>>>>>>> upstream/master
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
<<<<<<< HEAD
    product = Phone.objects.all().filter(slug=slug)
    context = {'product': product}
=======
    context = {}
>>>>>>> upstream/master
    return render(request, template, context)

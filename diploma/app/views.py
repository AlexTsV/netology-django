from django.shortcuts import render


# Create your views here.
def main(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def login(request):
    template = 'login.html',
    context = {}
    return render(request, template, context)


def cart(request):
    template = 'cart.html',
    context = {}
    return render(request, template, context)


def empty_section(request):
    template = 'empty_section.html',
    context = {}
    return render(request, template, context)


def smartphones(request):
    template = 'smartphones.html',
    context = {}
    return render(request, template, context)


def phone(request):
    template = 'phone.html',
    context = {}
    return render(request, template, context)

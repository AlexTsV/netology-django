from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.all()
    form = ReviewForm
    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }
    if pk in request.session['reviewed_products']:
        context['is_review_exist'] = True
    else:
        if request.method == 'POST':
            # логика для добавления отзыва
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = Review(text=form.cleaned_data['text'])
                review.save()
                request.session['reviewed_products'] = pk

    return render(request, template, context)

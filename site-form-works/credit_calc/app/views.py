from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    context = dict()
    if request.method == "GET":
        form = CalcForm(request.GET)
        if form.is_valid():
            common_result = form.cleaned_data['initial_fee'] + form.cleaned_data['initial_fee'] * form.cleaned_data['rate']
            context['common_result'] = common_result
            result = common_result / form.cleaned_data['months_count']
            context['result'] = result
            form = CalcForm
            context['form'] = form
            return render(request, template, context)

    else:
        form = CalcForm
    context = {
        'form': form
    }
    return render(request, template, context)

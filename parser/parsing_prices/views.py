from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'parsing_prices/index.html')


def about(request):
    return render(request, 'parsing_prices/about.html')


def company_data(request, company_id):
    return HttpResponse(f'<h2>Компания</h2><p>{company_id}</p>')

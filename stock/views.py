from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Stock
from django.template import RequestContext, loader
from produit.models import Product

# Create your views here.

def index(request):
    stocks = Stock.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'stocks':stocks,
    })
    return HttpResponse(template.render(context))

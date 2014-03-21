from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from stock.models import Product

# Create your views here.

def index(request):
    products = Product.objects.order_by("name")
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'products':products,
    })
    return HttpResponse(template.render(context))

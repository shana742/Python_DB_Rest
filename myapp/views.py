from django.shortcuts import render
from .models import ProductSubCat
from django.db.models import Q

# Create your views here.

def search(request):
    query = request.GET.get('q')
    if query:
        products = ProductSubCat.objects.filter(
            Q(product__product_name__icontains=query) |
            Q(product_model__icontains=query) |
            Q(product_price__icontains=query)
        )
    else:
        products = ProductSubCat.objects.all()
    return render(request, 'search.html',{'products': products})
	



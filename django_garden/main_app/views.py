from django.shortcuts import render
from .models import *

# Create your views here.
def main_page(request):
	product = Product.objects.all()
	context= {
		'products' : product,
	}
	return render(request, 'main_page.html', context)

def product(request, slug):
	product = Product.objects.get(slug=slug)
	advantages = Advantage.objects.filter(product=product)
	descriptions = Description.objects.filter(product=product)
	context = {
          'product':product,
          'advantages' : advantages,
          'descriptions' :descriptions,
          'products': Product.objects.all(),
    }
	return render(request, "product.html", context)
from django.shortcuts import render
from .models import *
from .form import OrderForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.
def main_page(request):
	product = Product.objects.all()
	comments = Comments.objects.all().order_by('-date')[:4]
	
	if request.method == 'POST':
		# Form was submitted
		form = OrderForm(request.POST)
		if form.is_valid():
			# Form fields passed validation
			cd = form.cleaned_data
			print(cd)
			# ... send email
			#return redirect('main_page')
			return HttpResponseRedirect(".")
		else:
			print(0)
	else:
		form = OrderForm()
	context= {
		'products' : product,
		'form':form,
		'comments':comments,
	}
	return render(request, 'main_page.html', context)

def product(request, slug):
	product = Product.objects.get(slug=slug)
	advantages = Advantage.objects.filter(product=product)
	descriptions = Description.objects.filter(product=product)
	form = OrderForm(request.POST)
	context = {
          'product':product,
          'advantages' : advantages,
          'descriptions' :descriptions,
          'products': Product.objects.all(),
          'form':form,
    }
	if request.method == 'POST':
		# Form was submitted
		
		if form.is_valid():
			# Form fields passed validation
			cd = form.cleaned_data
			print(cd)
			# ... send email
	return render(request, "product.html", context)
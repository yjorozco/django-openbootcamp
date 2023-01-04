from django.shortcuts import render, HttpResponse
from .models import Author, Entry

# Create your views here.

def queries(request):
	#obtener todos los elementos
	authors = Author.objects.all()

	#filtrar los elementos por condicion

	filtered = Author.objects.filter(email='christinavang@example.net')

	#obtener un unico objeto

	author = Author.objects.get(id=1)

	#obtener los 10 primeros elementos

	limits = Author.objects.all()[:10]

	# como podemos aplicar un offset
	# obtener 10 valores saltando los 5 primeros

	offsets = Author.objects.all()[5:10]

	#obtiene todos los elementos ordenados

	orders = Author.objects.all().order_by('email')

	#obtener todos los elementos cuyo id sea menor o igual a 15

	filtereds2 = Author.objects.filter(id__lte=15)

	#obtener  todos los autores que contienen en su nombre la palabra yes
    
	contains = Author.objects.filter(name__contains = "yes")

	return render(request, 'post/queries.html', { 'authors':authors, 'filtered':filtered, 'author': author, 'limits':limits, 'offsets': offsets, 'orders': orders, 'filtereds2':filtereds2, 'contains':contains})

def update(request):
	
	author = Author.objects.get(id=1)
	author.name = "Juanjo"
	author.email = "Juanjo@demo.com"
	author.save()
	return  HttpResponse('Modificado')
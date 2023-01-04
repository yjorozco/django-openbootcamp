
from django.shortcuts import render, HttpResponse


def getform(request):

	return render(request, 'form.html', {})


def getgoal(request):
	if request.method != 'GET':
		return HttpResponse('El metodo post no esta soportado para esta ruta')

	name = request.GET['name']

	return render(request, 'forms/success.html',{'name':name})


def postform(request):
	return render(request, 'postform.html',{})

def postgoal(request):
	if request.method!='POST':
		return HttpResponse('El metodo get no esta soportado para esta ruta')
	
	info = request.POST['info']
	return render(request, 'forms/postsuccess.html', {'info':info})
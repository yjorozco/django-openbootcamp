from django.shortcuts import render, HttpResponse
from .forms import EmployeeForm
# Create your views here.

def index(request):
	form = EmployeeForm()

	return render(request, 'index.html', {'form':form})
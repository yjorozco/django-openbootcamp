from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		#fields = ['name', 'last_name', 'email']
		#toma todos los campos
		fields = '__all__'
		#exclude = ('email',)
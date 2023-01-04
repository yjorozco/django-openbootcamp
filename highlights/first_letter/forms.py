from django.forms  import ModelForm

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		widgets = {
			'name': TextInput(attrs={'type':'text'})
		}

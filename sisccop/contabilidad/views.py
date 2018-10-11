from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'contabilidad/index.html')

def catalogoCuentas(request):
	return render(request,'contabilidad/catalogoCuentas.html')

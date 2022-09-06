from django.shortcuts import render, redirect
from .forms import TruckForm, CargoForm
from .models import Cargo

def home(request):
	return render(request, 'home.html',{})
def view_cargo (request):
	cargoList = Cargo.objects.all()
	return render(request, 'view_cargo.html', {'cargoList':cargoList})
def add_cargo (request):
	if request.method == 'POST':
		form = CargoForm(request.POST) ##TODO Change to CARGO

		if form.is_valid():
			form.save()
			print("saved")
			return redirect("home")
	else:
		print("not valid")
		form = CargoForm(request.POST) ##TODO Change to CARGOFORM
	return render(request, 'add_cargo.html', {'form':form})


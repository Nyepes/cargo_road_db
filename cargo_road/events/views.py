from django.shortcuts import render, redirect
from .forms import DriverForm, TruckForm, CargoForm, FedexSettlementForm
from .models import Cargo, Truck, FedexSettlement

def home(request):
	print(Truck.objects.filter(name = 'CR1')[0].id)
	return render(request, 'home.html',{})
def view_cargo (request):
	cargoList = Cargo.objects.all()
	return render(request, 'view_cargo.html', {'cargoList':cargoList})
def add_cargo (request):
	if request.method == 'POST':
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save(commit = False)
			cargo.truck = Truck.objects.filter(name = form.data['truck'])[0].id
			cargo.save()
			return redirect("home")
	else:
		form = CargoForm(request.POST)
	return render(request, 'add_cargo.html', {'form':form})

def add_truck(request):
	if request.method == 'POST':
		form = TruckForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	else:
		form = TruckForm(request.POST)
	return render(request, 'add_truck.html', {'form': form})

def add_fedex_settlement(request):
	if request.method == 'POST':
		form = FedexSettlementForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	else:
		form = FedexSettlementForm(request.POST)
	return render(request, 'fedex_settlement.html', {'form': form})
def add_driver(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	else:
		form = DriverForm(request.POST)
	return render(request, 'add_driver.html', {'form': form})



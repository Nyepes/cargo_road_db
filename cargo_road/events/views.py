from django.shortcuts import render, redirect
from .forms import DriverForm, DriverXCargoForm, TruckForm, CargoForm, FedexSettlementForm
from .models import Cargo, Driver, DriverXCargo, Truck, FedexSettlement
from django.db.models import Q
def home(request):
	print(Truck.objects.filter(name = 'CR1')[0].id)
	return render(request, 'home.html',{})
def view_cargo (request):
	cargoList = Cargo.objects.all()
	return render(request, 'view_cargo.html', {'cargoList':cargoList})
def add_cargo (request):
	form1 = DriverXCargoForm(request.POST)
	form2 = DriverXCargoForm(request.POST)
	if request.method == 'POST':
		form = CargoForm(request.POST)
		valid = form.is_valid() and form1.data['driver'] != form1.data['driver'] and form1.is_valid() and form2.is_valid()
		if valid:
			form.save()
			d1 = form1.save(commit = False)
			d2 = form2.save(commit = False)
			d1.shipment = form.get['shipment']
			d2.shipment = form.get['shipment']
			d1.save()
			d2.save()
			return redirect("home")
	else:
		form = CargoForm(request.POST)
	return render(request, 'add_cargo.html', {'form':form, 'form1': form1, 'form2': form2})

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
def driver_list(request):
	drivers = Driver.objects.order_by('name')
	return render(request, 'driver_list.html', {'drivers':drivers})
def truck_list(request):
	trucks = Truck.objects.order_by('name')
	return render(request, 'truck_list.html', {'trucks':trucks})
def detail_driver(request, did):
	driver = Driver.objects.get(pk=did)
	cargo = DriverXCargo.objects.filter(driver_id = did)
	return render(request, 'driver.html', {'driver':driver})
def update_driver(request, driver_id):
	driver = Driver.objects.get(pk=driver_id)
	form = DriverForm(request.POST or None, instance=driver)
	if request.method == 'POST':
		if (form.is_valid()):
			form.save()
			return redirect("home")
	return render(request, 'add_driver.html', {'form': form, 'driver':driver})



import time
from django.shortcuts import render, redirect
from .forms import Driver2XCargoForm, DriverForm, Driver1XCargoForm, TruckForm, CargoForm, FedexSettlementForm
from .models import Cargo, Driver, DriverXCargo, Truck, FedexSettlement
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
	print(Cargo.objects.first())
	print(Driver.objects.first())
	return render(request, 'home.html',{})
@login_required
def view_cargo (request):
	p = Paginator(Cargo.objects.all().order_by('id'), 25)
	page = request.GET.get('page')
	cargoList = p.get_page(page)
	return render(request, 'lists/view_cargo.html', {'cargoList':cargoList})
@login_required
def add_cargo (request):
	if request.method == 'POST':
		form = CargoForm(request.POST)
		print(form.data)
		if form.is_valid():
			cargo = form.save()
			print(cargo.id)
			form1 = Driver1XCargoForm(request.POST)
			form2 = Driver2XCargoForm(request.POST)
			form1.is_valid()
			form2.is_valid()
			try:
				dc1 = DriverXCargo(driver_cargo = cargo, dri = form1.clean()['dri'], percentage = form1.clean()['percentage']) 
				dc2 = DriverXCargo(driver_cargo = cargo, dri = form2.clean()['dri'], percentage = form2.clean()['percentage']) 
				dc1.save()
				dc2.save()
				return redirect('home')
			except:
				messages.success(request, str(form1.errors))
		else:
			messages.success(request, str(form.errors))
	form1 = Driver1XCargoForm(request.POST)
	form2 = Driver2XCargoForm(request.POST)
	form = CargoForm(request.POST)
	return render(request, 'create/add_cargo.html', {'form':form, 'form1': form1, 'form2': form2})
@login_required
def add_truck(request):
	if request.method == 'POST':
		form = TruckForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	form = TruckForm(request.POST)
	return render(request, 'create/add_truck.html', {'form': form})
@login_required
def add_fedex_settlement(request):
	if request.method == 'POST':
		form = FedexSettlementForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	else:
		form = FedexSettlementForm(request.POST)
	return render(request, 'create/fedex_settlement.html', {'form': form})
@login_required
def add_driver(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect("home")
	else:
		form = DriverForm(request.POST)
	return render(request, 'create/add_driver.html', {'form': form})
@login_required
def driver_list(request):
	drivers = Driver.objects.order_by('name')
	return render(request, 'lists/driver_list.html', {'drivers':drivers})
@login_required
def truck_list(request):
	trucks = Truck.objects.order_by('name')
	return render(request, 'lists/truck_list.html', {'trucks':trucks})
@login_required
def detail_driver(request, driver_id):
	driver = Driver.objects.get(pk=driver_id)
	#cargo = DriverXCargo.objects.filter(driver_id = did)
	return render(request, 'detail/driver.html', {'driver':driver})
@login_required
def detail_truck(request, truck_id):
	truck = Truck.objects.get(pk=truck_id)
	p = Paginator(Cargo.objects.filter(truck_id = truck_id).order_by('-pickup_date'),10)
	page = request.GET.get('page')
	cargo = p.get_page(page)
	
	return render(request, 'detail/view_truck.html', {'truck':truck, 'cargos':cargo})
@login_required
def update_driver(request, driver_id):
	driver = Driver.objects.get(pk=driver_id)
	form = DriverForm(request.POST or None, instance=driver)
	if request.method == 'POST':
		if (form.is_valid()):
			form.save()
			return redirect("home")
	return render(request, 'create/add_driver.html', {'form': form, 'driver':driver})
@login_required
def update_truck(request, truck_id):
	truck = Truck.objects.get(pk = truck_id)
	form = TruckForm(request.POST or None, instance=truck)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('home')
	return render (request,'create/add_truck.html',{'form':form})
@login_required
def detail_cargo(request, cargo_id):
	cargo = Cargo.objects.get(pk = cargo_id)
	return render(request, 'detail/cargo.html', {'cargo':cargo})


from django.shortcuts import render, redirect
from .forms import Driver2XCargoForm, DriverForm, Driver1XCargoForm, TruckForm, CargoForm, FedexSettlementForm
from .models import Cargo, Driver, DriverXCargo, Truck, FedexSettlement

def home(request):
	print(Cargo.objects.first())
	print(Driver.objects.first())
	return render(request, 'home.html',{})
def view_cargo (request):
	cargoList = Cargo.objects.all()
	return render(request, 'view_cargo.html', {'cargoList':cargoList})
def add_cargo (request):
	if request.method == 'POST':
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			form1 = Driver1XCargoForm(request.POST, initial={'shipment':cargo})
			form2 = Driver2XCargoForm(request.POST, initial={'shipment':cargo})
			if form1.is_valid() and form2.is_valid():
				form1.save()
				form2.save()
				return redirect("home")
	form1 = Driver1XCargoForm(request.POST)
	form2 = Driver2XCargoForm(request.POST)
	form = CargoForm(request.POST)
	return render(request, 'add_cargo.html', {'form':form, 'form1': form1, 'form2': form2})

def load_driver(request):
    driver_id = request.GET.get('driver')
    driver_percent = DriverXCargo.objects.filter(driver=driver_id).latest('percentage')
    return render(request, 'add_cargo.html', {'percentage': driver_percent})
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
def detail_driver(request, driver_id):
	driver = Driver.objects.get(pk=driver_id)
	#cargo = DriverXCargo.objects.filter(driver_id = did)
	return render(request, 'driver.html', {'driver':driver})
def detail_truck(request, truck_id):
	truck = Truck.objects.get(pk=truck_id)
	#cargo = DriverXCargo.objects.filter(driver_id = did)
	return render(request, 'view_truck.html', {'truck':truck})
def update_driver(request, driver_id):
	driver = Driver.objects.get(pk=driver_id)
	form = DriverForm(request.POST or None, instance=driver)
	if request.method == 'POST':
		if (form.is_valid()):
			form.save()
			return redirect("home")
	return render(request, 'add_driver.html', {'form': form, 'driver':driver})



from django.db import models


# Class Truck with attributes
# name: CR + id.  (ie. CR1)
# plate: Liscnece plate
# Standard C Link
# Standard Insurance
class Truck (models.Model):
	name = models.CharField(max_length=8)
	plate = models.CharField(max_length=8)
	standard_c_link = models.DecimalField(decimal_places=2,max_digits=5,default=0)
	standard_insurance = models.DecimalField(decimal_places=2,max_digits=6,default=0)

class FedexSettlement (models.Model):
	settlement_fedex = models.PositiveIntegerField()
	settlement_date = models.DateField()
	fedex_payment_date =  models.DateField()
	applicant_cost = models.DecimalField(decimal_places=2,max_digits=6,default=0)
	personal_insurance = models.DecimalField(decimal_places=2,max_digits=7,default=0)
	modelsadjust = models.DecimalField(decimal_places=2,max_digits=8,default=0)


class TruckFedexSettlement (models.Model):
	settlement_fedex = models.ForeignKey(FedexSettlement, on_delete = models.CASCADE) # Repasar on delete methods
	truck_id = models.ForeignKey(Truck, on_delete = models.CASCADE)
	c_link = models.DecimalField(decimal_places=2, max_digits=10, default=0) #Check if decimal places make sense
	mileage_taxes =  models.DecimalField(decimal_places=2, max_digits=10, default=0)
	fuel_taxes = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	other_costs = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	scrow = models.DecimalField(decimal_places=2, max_digits=10, default=0)

class DriverSettlement (models.Model):
	settlement_drivers = models.PositiveIntegerField()
	pay_date = models.DateField()

class Cargo (models.Model):
	shipment = models.PositiveIntegerField()
	truck = models.ForeignKey(Truck, on_delete = models.CASCADE) #hablar con papi sobre on delete
	driver_settlement = models.ForeignKey(DriverSettlement, on_delete = models.CASCADE)
	fedex_settlement = models.ForeignKey(FedexSettlement, on_delete = models.CASCADE)
	description = models.CharField(max_length = 300) #Change max length
	pickup_date = models.DateField()
	delivery_date = models.DateField(blank = True)
	load_miles = models.PositiveSmallIntegerField()
	loaded_income = models.DecimalField(decimal_places = 2, max_digits = 10)
	fuel_surcharge = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	tolls_surcharge = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	dhpu = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	empty_income = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	t_check_advance = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	traded_value = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	detention = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	state = models.CharField(max_length = 20)

class Driver (models.Model):
	driver_id = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	w2 = models.BooleanField()
	driver_id_fedex = models.PositiveIntegerField()
	standard_pay = models.PositiveSmallIntegerField()

class DriverXCargo(models.Model):
	shipment = models.ForeignKey(Cargo, on_delete = models.CASCADE)
	driver_id = models.ForeignKey(Driver, on_delete = models.CASCADE)
	percentage = models.PositiveSmallIntegerField()

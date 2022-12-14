from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Sum
# Class Truck with attributes
# name: CR + id.  (ie. CR1)
# plate: Liscnece plate
# Standard C Link
# Standard Insurance
class Truck (models.Model):
	name = models.CharField(max_length=8,blank=True) #No se si dejar o volver una calculated property?
	plate = models.CharField(max_length=8,blank=True)
	standard_c_link = models.DecimalField(decimal_places=2,max_digits=10,default=0,blank=True)
	standard_insurance = models.DecimalField(decimal_places=2,max_digits=10,default=0,blank=True)
	@property
	def total_miles(self):
		return Cargo.objects.filter(truck_id = self.id).aggregate(Sum('load_miles')).get('load_miles__sum', 0.00)
	def __str__(self):
		return self.name

class FedexSettlement (models.Model):
	settlement_fedex = models.PositiveIntegerField()
	settlement_date = models.DateField()
	fedex_payment_date =  models.DateField()
	applicant_cost = models.DecimalField(decimal_places=2,max_digits=6,default=0)
	personal_insurance = models.DecimalField(decimal_places=2,max_digits=7,default=0)
	adjust = models.DecimalField(decimal_places=2,max_digits=8,default=0)
	def __str__(self):
		return str(self.settlement_fedex)

class TruckFedexSettlement (models.Model):
	settlement_fedex = models.ForeignKey(FedexSettlement, on_delete = models.CASCADE) # Repasar on delete methods
	truck_id = models.ForeignKey(Truck, on_delete = models.CASCADE)
	c_link = models.DecimalField(decimal_places=2, max_digits=10, default=0) #Check if decimal places make sense
	mileage_taxes =  models.DecimalField(decimal_places=2, max_digits=10, default=0)
	fuel_taxes = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	other_costs = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	scrow = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	def __str__(self):
		return str(self.settlement_fedex)
class DriverSettlement (models.Model):
	settlement_drivers = models.PositiveIntegerField()
	pay_date = models.DateField()
	def __str__(self):
		return str(self.settlement_drivers)

class Cargo (models.Model):
	shipment = models.PositiveBigIntegerField(unique=True)
	truck = models.ForeignKey(Truck, on_delete = models.CASCADE) #hablar con papi sobre on delete
	driver_settlement = models.ForeignKey(DriverSettlement, on_delete = models.CASCADE,  blank = True, null=True)
	fedex_settlement = models.ForeignKey(FedexSettlement,   on_delete = models.CASCADE, blank = True, null=True)
	description = models.CharField( max_length = 300) #Change max length
	pickup_date = models.DateField()
	delivery_date = models.DateField()
	load_miles = models.PositiveSmallIntegerField(blank = True)
	loaded_income = models.DecimalField( decimal_places = 2, max_digits = 10)
	fuel_surcharge = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	tolls_surcharge = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	dhpu = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	empty_income = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	t_check_advance = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	traded_value = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	detention = models.DecimalField( decimal_places = 2, max_digits = 10, default = 0)
	state = models.CharField( max_length = 20)

class Driver (models.Model):
	nickname = models.CharField(max_length=20, blank=True)
	name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	w2 = models.BooleanField()
	driver_id_fedex = models.PositiveIntegerField(blank=True)
	standard_pay = models.PositiveSmallIntegerField(blank=True)
	def __str__(self):
		return self.name + " " + self.last_name + " | " + self.nickname

class DriverXCargo(models.Model):
	driver_cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE)
	dri = models.ForeignKey(Driver, on_delete = models.CASCADE)
	percentage = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

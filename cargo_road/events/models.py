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


from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Cargo, Truck, FedexSettlement

class TruckForm(ModelForm):
	class Meta:
		model = Truck
		fields = ('name', 'plate', 'standard_c_link', 'standard_insurance')
		labels = {
			"name": "Name",
			"plate": "Liscence Plate",
			"standard_c_link": "Standard C Link",
			"standard_insurance": "Standard Insurance"
		}
		widgets = {
			"name": forms.TextInput(attrs={'class':'form-control','required': 'True'}),
			"plate": forms.TextInput(attrs={'class':'form-control','required': 'True'}),
			"standard_c_link": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'C Link'}),
			"standard_insurance": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Standard Insurance'})
		}
class FedexSettlementForm(ModelForm):
	class Meta:
		model = FedexSettlement
		fields = ('settlement_fedex', "settlement_date", "fedex_payment_date", 'applicant_cost',
			'personal_insurance','adjust')
		labels = {
			'settlement_fedex': "Settlement Fedex",
			"settlement_date": "Settlement Date",
			"fedex_payment_date": "Fedex Payment Date",
			'applicant_cost': "Applicant Cost",
			'personal_insurance': "Personal Insurance",
			'adjust': "Adjust"
		}
		widgets = {
			'settlement_fedex': forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Settlement Fedex'}),
			'settlement_date': forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
			'fedex_payment_date': forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
			'applicant_cost': forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Applicant Cost'}),
			'personal_insurance': forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Personal Insurance'}),
			'adjust': forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Adjust'}),
		}
class CargoForm(ModelForm):
	class Meta:
		model = Cargo
		fields = ('shipment', 'truck','driver_settlement', 'fedex_settlement', 'description','pickup_date', 
		'delivery_date', 'load_miles', 'loaded_income', 'fuel_surcharge', 'tolls_surcharge', 'dhpu',
		'empty_income', 't_check_advance', 'traded_value', 'detention', 'state')

		labels = {
			'shipment': "Shipment",
			'truck': "Truck",
			'driver_settlement': "Driver Settlement",
			'fedex_settlement': "Fedex Settlement",
			'description': "Description",
			'pickup_date': "Pickup Date",
			'delivery_date': "Delivery Date",
			'load_miles': "Load Miles",
			'loaded_income': "Loaded Income",
			'fuel_surcharge': "Fuel Surcharge",
			'tolls_surcharge': "Tolls Surcharge",
			'dhpu': "DHPU",
			'empty_income': "Empty Income",
			't_check_advance': "T Check Advance",
			'traded_value': "Traded Value",
			'detention': "Detention",
			'state': "State"
		}
		widgets = {
			'shipment': forms.NumberInput(attrs={'class':'form-control','required': 'True' }),
			#Cambiar a Select y cambiar de nombre a id en views
			'truck': forms.Select(attrs={'class':'form-control','required': 'True', 'placeholder':'Truck'}),
			#Cambiar a Select y add filter somehow
			'driver_settlement':forms.Select(attrs={'class':'form-control','required': 'True', 'placeholder':'Truck'}),
			#Cambiar a Select y add filter somehow
			'fedex_settlement': forms.Select(attrs={'class':'form-control','required': 'True'}),
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'pickup_date': forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
			'delivery_date': forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
			'load_miles': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'loaded_income': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'fuel_surcharge': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'tolls_surcharge': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'dhpu': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'empty_income': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			't_check_advance': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'traded_value': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'detention': forms.NumberInput(attrs={'class':'form-control','required': 'True', }),
			'state': forms.TextInput(attrs={'class':'form-control','required': 'True'}),
		}


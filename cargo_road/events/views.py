from django.shortcuts import render
from .models import Cargo

def home(request):
	return render(request, 'home.html',{})
def view_cargo (request):
	cargoList = Cargo.objects.all()
	return render(request, 'view_cargo.html', {'cargoList':cargoList})
def add_cargo (request):
	return render(request, 'add_cargo.html', {})

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('view-cargo', views.view_cargo, name = "view_cargo"),
    path('add-cargo', views.add_cargo, name = "add_cargo"),
    path('add-truck', views.add_truck,name = 'add_truck'),
    path('add-fedex-settlement', views.add_fedex_settlement,name = 'add_fedex_settlement'),
    path('add-driver', views.add_driver,name = 'add_driver'),
]

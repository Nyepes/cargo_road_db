from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('view-cargo', views.view_cargo, name = "view_cargo"),
    path('add-cargo', views.add_cargo, name = "add_cargo"),
    path('add-truck', views.add_truck,name = 'add_truck'),
    path('add-fedex-settlement', views.add_fedex_settlement,name = 'add_fedex_settlement'),
    path('add-driver', views.add_driver,name = 'add_driver'),
    path('driver-list',views.driver_list,name="view_drivers"),
    path('truck-list',views.truck_list,name="view_trucks"),
    path('detail-driver<driver_id>', views.detail_driver, name='detail_driver'),
    path('update-driver<driver_id>',views.update_driver,name='update_driver'),
    path('detail-truck<truck_id>', views.detail_truck, name='detail_truck'),
    path('update-truck<truck_id>', views.update_truck, name='update_truck'),
    path('ajax/get-driver/', views.load_driver, name='ajax_load_driver'),
]

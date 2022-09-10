from django.contrib import admin

from events.models import Cargo, DriverSettlement, DriverXCargo

admin.site.register(DriverXCargo)
admin.site.register(DriverSettlement)
admin.site.register(Cargo)


# @admin.register(DriverXCargo)
# class DriverXCargoAdmin(admin.ModelAdmin):
#     list_display = ('driver','percentage','shipment')
# Generated by Django 4.1.1 on 2022-09-16 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_cargo_id_driverxcargo_shipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverxcargo',
            old_name='shipment',
            new_name='driver_cargo',
        ),
    ]

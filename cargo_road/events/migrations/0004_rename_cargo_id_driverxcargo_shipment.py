# Generated by Django 4.1.1 on 2022-09-12 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_shipment_driverxcargo_cargo_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverxcargo',
            old_name='cargo_id',
            new_name='shipment',
        ),
    ]
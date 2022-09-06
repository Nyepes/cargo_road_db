# Generated by Django 4.1.1 on 2022-09-06 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FedexSettlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settlement_fedex', models.PositiveIntegerField()),
                ('settlement_date', models.DateField()),
                ('fedex_payment_date', models.DateField()),
                ('applicant_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('personal_insurance', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('modelsadjust', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('plate', models.CharField(max_length=8)),
                ('standard_c_link', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('standard_insurance', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='TruckFedexSettlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_link', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mileage_taxes', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fuel_taxes', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('other_costs', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('scrow', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('settlement_fedex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.fedexsettlement')),
                ('truck_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.truck')),
            ],
        ),
    ]

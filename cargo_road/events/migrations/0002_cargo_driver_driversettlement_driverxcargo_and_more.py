# Generated by Django 4.1.1 on 2022-09-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=300)),
                ('pickup_date', models.DateField()),
                ('delivery_date', models.DateField(blank=True)),
                ('load_miles', models.PositiveSmallIntegerField()),
                ('loaded_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuel_surcharge', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tolls_surcharge', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dhpu', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('empty_income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('t_check_advance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('traded_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('detention', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('w2', models.BooleanField()),
                ('driver_id_fedex', models.PositiveIntegerField()),
                ('standard_pay', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DriverSettlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settlement_drivers', models.PositiveIntegerField()),
                ('pay_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DriverXCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveSmallIntegerField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.driver')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.cargo')),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='driver_settlement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.driversettlement'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='fedex_settlement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.fedexsettlement'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.truck'),
        ),
    ]

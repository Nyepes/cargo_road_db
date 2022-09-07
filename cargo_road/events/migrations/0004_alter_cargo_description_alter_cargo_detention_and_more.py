# Generated by Django 4.1.1 on 2022-09-07 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_fedexsettlement_modelsadjust_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='detention',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='dhpu',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='driver_settlement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.driversettlement'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='empty_income',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='fedex_settlement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.fedexsettlement'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='fuel_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='load_miles',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='loaded_income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='pickup_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='shipment',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='t_check_advance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='tolls_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='traded_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='truck',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.truck'),
        ),
    ]
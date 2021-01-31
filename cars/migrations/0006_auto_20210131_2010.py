# Generated by Django 3.1.5 on 2021-01-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20210130_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Bensin', 'Bensin'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('EL', 'EL'), ('Bensin', 'Bensin'), ('Ethanol', 'Ethanol')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Automatic ', 'Automatic'), ('Manual', 'Manual')], max_length=10),
        ),
    ]

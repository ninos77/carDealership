# Generated by Django 3.1.5 on 2021-01-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[], verbose_name='year'),
        ),
    ]
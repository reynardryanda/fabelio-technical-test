# Generated by Django 3.0.7 on 2020-06-21 07:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_db_constraints.operations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MSTProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)])),
                ('dimension', models.CharField(max_length=15)),
                ('material', models.CharField(max_length=20)),
                ('max_seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TRXProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('mst_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='database.MSTProduct')),
            ],
            options={
                'unique_together': {('mst_product', 'color')},
            },
        ),
        django_db_constraints.operations.AlterConstraints(
            name='MSTProduct',
            db_constraints={'max_seats_above_zero': 'check (max_seats>0)', 'price_above_zero': 'check (price>0)'},
        ),
        django_db_constraints.operations.AlterConstraints(
            name='TRXProduct',
            db_constraints={'quantity_not_negative': 'check (quantity>=0)'},
        ),
    ]

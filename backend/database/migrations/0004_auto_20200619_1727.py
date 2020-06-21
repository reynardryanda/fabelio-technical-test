# Generated by Django 3.0.7 on 2020-06-19 10:27

import django.core.validators
from django.db import migrations, models
import django_db_constraints.operations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20200619_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='mstproduct',
            name='max_seats',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        django_db_constraints.operations.AlterConstraints(
            name='mstproduct',
            db_constraints={'max_seats_above_zero': 'check (max_seats>0)', 'price_above_zero': 'check (price>0)'},
        ),
    ]
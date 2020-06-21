# Generated by Django 3.0.7 on 2020-06-19 08:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TRXProduct',
            fields=[
                ('color', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('mst_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MSTProduct')),
            ],
            options={
                'unique_together': {('mst_product', 'color')},
            },
        ),
    ]
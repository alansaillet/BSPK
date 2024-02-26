# Generated by Django 5.0.2 on 2024-02-25 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurnitureConfigurator', '0005_remove_furniture_height2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='chairbacktype',
            field=models.CharField(choices=[('flat', 'Flat Back'), ('rods', 'With Rods')], default='flat', max_length=50),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='furnituretype',
            field=models.CharField(choices=[('chair', 'Chaise1'), ('table', 'Table1')], default='chair', max_length=50),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='height',
            field=models.FloatField(default=80, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(130)]),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='length',
            field=models.FloatField(default=130, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(250)]),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='nbrods',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='thickness_backchair',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='width',
            field=models.FloatField(default=50, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(250)]),
        ),
    ]
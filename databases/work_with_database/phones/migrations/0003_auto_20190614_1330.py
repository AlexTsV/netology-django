# Generated by Django 2.0.5 on 2019-06-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20190614_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 2.0.5 on 2019-06-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(upload_to='products/%Y/%m/%d/'),
        ),
    ]

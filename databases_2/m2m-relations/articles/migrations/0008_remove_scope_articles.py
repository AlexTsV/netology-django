# Generated by Django 2.0.5 on 2019-06-20 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190620_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
    ]
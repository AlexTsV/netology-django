# Generated by Django 2.1 on 2019-06-29 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190629_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.Article'),
        ),
    ]

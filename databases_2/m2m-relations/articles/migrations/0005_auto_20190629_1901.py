# Generated by Django 2.1 on 2019-06-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190629_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articles',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.Scope'),
        ),
    ]

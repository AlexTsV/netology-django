# Generated by Django 2.0.5 on 2019-06-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190620_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Article'),
        ),
    ]
# Generated by Django 2.1 on 2019-06-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190629_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Scope'),
        ),
    ]

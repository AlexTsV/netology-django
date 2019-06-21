# Generated by Django 2.0.5 on 2019-06-20 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20190620_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основная')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutscope',
            name='article',
        ),
        migrations.RemoveField(
            model_name='aboutscope',
            name='scope',
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_scopes',
        ),
        migrations.AlterField(
            model_name='scope',
            name='topic',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='AboutScope',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Новости'),
        ),
        migrations.AddField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Scope', verbose_name='Категории'),
        ),
    ]
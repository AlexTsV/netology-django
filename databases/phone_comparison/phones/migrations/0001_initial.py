# Generated by Django 2.0.5 on 2019-06-13 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField()),
                ('OS', models.TextField()),
                ('screen', models.TextField()),
                ('camera', models.TextField()),
                ('RAM', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.TextField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.TextField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='apple',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
    ]

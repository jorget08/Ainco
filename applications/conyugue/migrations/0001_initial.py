# Generated by Django 3.2 on 2021-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conyugue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('correo', models.EmailField(max_length=254)),
                ('empresa_labora', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=10)),
                ('cargo', models.CharField(max_length=70)),
                ('fijo', models.CharField(blank=True, max_length=7)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-07-11 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresaSocia', '0002_alter_empresasocia_deudores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresasocia',
            name='deudores',
        ),
    ]

# Generated by Django 3.2 on 2021-05-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deudor', '0005_auto_20210527_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deudor',
            name='estado_inicial',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

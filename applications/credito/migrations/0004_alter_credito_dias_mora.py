# Generated by Django 3.2 on 2021-05-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0003_credito_vencido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='dias_mora',
            field=models.SmallIntegerField(),
        ),
    ]

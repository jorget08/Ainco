# Generated by Django 3.2 on 2021-05-20 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0009_credito_normalizado'),
        ('codeudor', '0004_auto_20210520_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeudor',
            name='credito',
        ),
        migrations.AddField(
            model_name='codeudor',
            name='credito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='credito.credito'),
        ),
    ]

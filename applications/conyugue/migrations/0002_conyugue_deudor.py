# Generated by Django 3.2 on 2021-05-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conyugue', '0001_initial'),
        ('deudor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conyugue',
            name='deudor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deudor.deudor'),
        ),
    ]
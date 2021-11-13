# Generated by Django 3.2 on 2021-05-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credito', '0001_initial'),
        ('deudor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='deudor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credito_deudor', to='deudor.deudor'),
        ),
    ]
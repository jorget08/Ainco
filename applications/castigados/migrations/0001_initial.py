# Generated by Django 3.2 on 2022-03-04 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deudor', '0009_auto_20210910_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastigoCartera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('archivo', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('archivo2', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('archivo3', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('archivo4', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('archivo5', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('archivo6', models.FileField(blank=True, upload_to='documentosDeudores')),
                ('calificacion_viabilidad', models.CharField(choices=[('0', 'Viable'), ('1', 'No viable')], max_length=2)),
                ('observaciones', models.TextField(blank=True)),
                ('usuario', models.CharField(blank=True, max_length=15)),
                ('deudor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='castigo_deudor', to='deudor.deudor')),
            ],
        ),
    ]
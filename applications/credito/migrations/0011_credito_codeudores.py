# Generated by Django 3.2 on 2021-05-21 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeudor', '0006_remove_codeudor_credito'),
        ('credito', '0010_alter_credito_codigo_credito'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='codeudores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credito_codeudor', to='codeudor.codeudor'),
        ),
    ]

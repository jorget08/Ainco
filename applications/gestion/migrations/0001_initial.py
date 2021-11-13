# Generated by Django 3.2 on 2021-04-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_contactada', models.CharField(choices=[('0', 'Deudor'), ('1', 'Codeudor'), ('2', 'Familiar'), ('3', 'Referencia')], max_length=2)),
                ('fecha_gestion', models.DateField(auto_now_add=True)),
                ('nombre_parentesco', models.CharField(max_length=100)),
                ('tipo_gestion', models.CharField(choices=[('0', 'Llamada a celular'), ('0', 'Llamada a celular'), ('2', 'Mensaje de texto'), ('3', 'Mensaje de whatsapp'), ('4', 'Envio de correo electronico'), ('5', 'Visita al domicilio'), ('6', 'Visita a la empresa')], max_length=2)),
                ('resultado_gestion', models.CharField(choices=[('0', 'Establece acuerdo de pago'), ('1', 'Visitará la oficina'), ('2', 'Volver a llamar'), ('4', 'Solicita cambio de fecha de pago'), ('5', 'Cumplio con el acuerdo de pago'), ('6', 'No cumplio con el acuerdo de pago'), ('5', 'Visita al domicilio'), ('6', 'Visita a la empresa')], max_length=200)),
                ('observaciones', models.TextField()),
                ('causales_no_pago', models.CharField(choices=[('0', 'Desempleo'), ('1', 'Disminición de ingresos'), ('2', 'Problemas familiares'), ('3', 'Se encuentra incapacitado'), ('4', 'Otros')], max_length=2)),
                ('califiacion_viabilidad', models.CharField(choices=[('0', 'Viable'), ('1', 'No viable')], max_length=2)),
                ('fecha_nueva_accion', models.DateField()),
                ('nueva_accion', models.CharField(choices=[('0', 'Llamar al fijo'), ('1', 'Llamar al celular'), ('2', 'Enviar mensaje de texto'), ('3', 'Enviar mensaje por whatsapp'), ('4', 'Enviar correo electrónico'), ('5', 'Visitar al domicilio'), ('6', 'Visitar en la empresa'), ('7', 'Atención en la oficina'), ('8', 'Seguimiento al acuerdo de pago')], max_length=2)),
                ('hora_nueva_accion', models.TimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
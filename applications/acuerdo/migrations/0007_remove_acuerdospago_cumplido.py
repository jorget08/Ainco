# Generated by Django 3.2 on 2021-12-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acuerdo', '0006_alter_acuerdospago_estado_del_acuerdo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acuerdospago',
            name='cumplido',
        ),
    ]
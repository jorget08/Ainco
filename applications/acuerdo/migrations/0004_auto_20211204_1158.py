# Generated by Django 3.2 on 2021-12-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acuerdo', '0003_acuerdospago_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='acuerdospago',
            name='cumplido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='acuerdospago',
            name='estado_del_acuerdo',
            field=models.BooleanField(default=True),
        ),
    ]
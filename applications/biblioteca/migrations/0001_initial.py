# Generated by Django 3.2 on 2021-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilbio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('fecha_vigencia', models.DateField()),
                ('tema', models.CharField(max_length=200)),
                ('documento', models.FileField(blank=True, upload_to='biblioteca')),
            ],
        ),
    ]
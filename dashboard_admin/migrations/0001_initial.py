# Generated by Django 5.1.3 on 2024-11-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcercaDe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mision', models.TextField()),
                ('ubicacion', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('whatsapp', models.CharField(max_length=255)),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hoteles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hotelname', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('precio_antes', models.DecimalField(decimal_places=5, max_digits=10)),
                ('precio_ahora', models.DecimalField(decimal_places=5, max_digits=10)),
                ('imagen_uno', models.BinaryField()),
                ('imagen_dos', models.BinaryField()),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0002_hoteles_ciudad_alter_hoteles_precio_ahora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteles',
            name='visitas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

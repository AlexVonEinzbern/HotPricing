# Generated by Django 4.2.1 on 2023-06-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteles',
            name='ciudad',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hoteles',
            name='precio_ahora',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='hoteles',
            name='precio_antes',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
    ]
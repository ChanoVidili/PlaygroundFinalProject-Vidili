# Generated by Django 4.2.3 on 2023-09-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLigaDeFutbol', '0014_remove_jugador_imagen_imagenjugador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='assets/img/jugadores'),
        ),
        migrations.DeleteModel(
            name='ImagenJugador',
        ),
    ]

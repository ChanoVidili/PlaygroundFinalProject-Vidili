# Generated by Django 4.2.3 on 2023-09-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLigaDeFutbol', '0012_jugador_imagen_jugador_alter_avatar_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='imagen_jugador',
        ),
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='assets/img/jugadores', verbose_name='Imagen'),
        ),
    ]

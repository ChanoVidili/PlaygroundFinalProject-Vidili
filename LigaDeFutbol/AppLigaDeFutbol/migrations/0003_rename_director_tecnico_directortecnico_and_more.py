# Generated by Django 4.2.3 on 2023-08-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLigaDeFutbol', '0002_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Director_Tecnico',
            new_name='DirectorTecnico',
        ),
        migrations.AddField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(default=80, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jugador',
            name='promedio',
            field=models.IntegerField(default=80),
        ),
    ]
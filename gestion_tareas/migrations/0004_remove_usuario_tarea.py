# Generated by Django 4.1.1 on 2022-09-09 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_tareas", "0003_usuario_tarea"),
    ]

    operations = [
        migrations.RemoveField(model_name="usuario", name="tarea",),
    ]
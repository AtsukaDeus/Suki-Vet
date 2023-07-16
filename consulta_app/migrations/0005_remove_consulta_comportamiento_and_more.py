# Generated by Django 4.2.1 on 2023-07-15 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta_app', '0004_consulta_comportamiento_consulta_movilidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='comportamiento',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='movilidad',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='pelaje',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='piel',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='postura',
        ),
        migrations.AddField(
            model_name='consulta',
            name='evaluacion_general',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]

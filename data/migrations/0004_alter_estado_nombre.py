# Generated by Django 5.1.4 on 2025-01-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_estado_alter_casocorrupcion_comuna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(choices=[('En Proceso', 'En Proceso'), ('Resuelto', 'Resuelto'), ('Cerrado', 'Cerrado'), ('En Investigación', 'En Investigación'), ('Formalizado', 'Formalizado'), ('Sentenciado', 'Sentenciado'), ('Condenado', 'Condenado')], default='En Proceso', max_length=255),
        ),
    ]

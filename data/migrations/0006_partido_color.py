# Generated by Django 5.1.4 on 2025-01-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_casocorrupcion_responsable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='color',
            field=models.CharField(default='#000000', help_text='Color en formato HEX (ej: #FF0000)', max_length=7),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_partido_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='color',
        ),
        migrations.AddField(
            model_name='sector',
            name='color',
            field=models.CharField(default='#000000', help_text='Color en formato HEX (ej: #FF0000)', max_length=7),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-26 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_content_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order'], 'verbose_name': 'Контент', 'verbose_name_plural': 'Контенты'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order'], 'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
    ]

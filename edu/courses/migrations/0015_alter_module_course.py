# Generated by Django 5.1.4 on 2024-12-27 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_module_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course', verbose_name='Курс'),
        ),
    ]

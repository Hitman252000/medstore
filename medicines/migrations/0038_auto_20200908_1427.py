# Generated by Django 3.1 on 2020-09-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0037_auto_20200908_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='slug',
            field=models.SlugField(default='se.ljdn<aaeDiil', unique=True),
        ),
    ]

# Generated by Django 3.1 on 2020-09-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0034_auto_20200908_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='slug',
            field=models.SlugField(default='alonfisFlm.f.eb', unique=True),
        ),
    ]

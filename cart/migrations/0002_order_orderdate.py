# Generated by Django 3.1 on 2020-08-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2022-01-24 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='customer',
        ),
    ]
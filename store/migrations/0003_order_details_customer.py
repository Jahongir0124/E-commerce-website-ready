# Generated by Django 3.2.7 on 2022-01-24 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_order_details_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CallCenter_App', '0004_paidcustomer_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidcustomer',
            name='customer_id',
            field=models.CharField(editable=False, max_length=12),
        ),
    ]

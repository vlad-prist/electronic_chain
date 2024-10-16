# Generated by Django 5.1.2 on 2024-10-16 08:00

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0002_remove_retailer_factory_remove_trader_factory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True, verbose_name='задолженность'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True, verbose_name='задолженность'),
        ),
        migrations.AlterField(
            model_name='trader',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True, verbose_name='задолженность'),
        ),
    ]

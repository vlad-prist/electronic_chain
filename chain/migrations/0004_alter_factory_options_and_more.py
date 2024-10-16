# Generated by Django 5.1.2 on 2024-10-16 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0003_alter_factory_debt_alter_retailer_debt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'производитель', 'verbose_name_plural': 'производители'},
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='provider_retailer',
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='provider_trader',
        ),
        migrations.RemoveField(
            model_name='trader',
            name='provider_trader',
        ),
        migrations.AlterField(
            model_name='retailer',
            name='provider_factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplied_retailers', to='chain.factory'),
        ),
        migrations.AlterField(
            model_name='trader',
            name='provider_factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_for_traders', to='chain.factory'),
        ),
        migrations.AlterField(
            model_name='trader',
            name='provider_retailer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_for_traders', to='chain.retailer'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-14 09:18

import gnosis.eth.django.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "chains",
            "0011_rename_min_master_copy_version_chain_recommended_master_copy_version",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="gas_price_fixed_wei",
            field=gnosis.eth.django.models.Uint256Field(
                blank=True, null=True, verbose_name="Fixed gas price (wei)"
            ),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_cash_transfer_to_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_transfer',
            name='cash_remark',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
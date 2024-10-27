# Generated by Django 5.1.2 on 2024-10-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_cash_amount_user_cash_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_transfer',
            name='admin_verify_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cash_transfer',
            name='office_verify_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cash_transfer',
            name='self_verify_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cash_transfer',
            name='to_verify_status',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_phonepe_transition'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_account',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
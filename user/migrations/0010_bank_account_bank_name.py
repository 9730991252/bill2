# Generated by Django 5.1.2 on 2024-10-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_account',
            name='bank_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_phonepe_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonepe',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]

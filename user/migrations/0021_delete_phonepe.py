# Generated by Django 5.1.2 on 2024-10-23 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_remove_phonepe_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Phonepe',
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-24 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_bank_transition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank_transition',
            old_name='phonepe',
            new_name='bank',
        ),
    ]
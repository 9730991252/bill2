# Generated by Django 5.1.2 on 2024-10-26 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_cash_transfer_admin_verify_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonepe_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_phonepe_id', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('self_verify_status', models.IntegerField(default=0)),
                ('office_verify_status', models.IntegerField(default=0)),
                ('admin_verify_status', models.IntegerField(default=0)),
                ('to_verify_status', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('to_phonepe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.phonepe')),
            ],
        ),
    ]
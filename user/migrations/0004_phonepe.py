# Generated by Django 5.1.2 on 2024-10-22 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_amount_user_cash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]

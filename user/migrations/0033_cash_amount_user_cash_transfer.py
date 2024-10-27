# Generated by Django 5.1.2 on 2024-10-25 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_user_out_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_amount',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.CreateModel(
            name='Cash_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user_cash')),
            ],
        ),
    ]
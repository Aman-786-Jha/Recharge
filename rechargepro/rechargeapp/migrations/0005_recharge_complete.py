# Generated by Django 4.1.5 on 2023-01-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rechargeapp', '0004_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]

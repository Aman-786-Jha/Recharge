# Generated by Django 4.1.5 on 2023-01-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rechargeapp', '0011_alter_carddetails_integrity'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroUnlimited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talktime', models.TextField()),
                ('data', models.TextField()),
                ('validity', models.IntegerField()),
                ('additional_benefit', models.CharField(blank=True, max_length=150)),
                ('price', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherPacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talktime', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talktime', models.TextField()),
                ('calls', models.CharField(max_length=20)),
                ('SMS', models.CharField(blank=True, max_length=20)),
                ('validity', models.TextField()),
                ('additional_benefit', models.CharField(blank=True, max_length=100)),
                ('price', models.TextField()),
            ],
        ),
    ]

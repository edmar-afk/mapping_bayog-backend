# Generated by Django 5.0.6 on 2025-06-19 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_seniorcitizen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Households',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='api.households')),
            ],
        ),
    ]

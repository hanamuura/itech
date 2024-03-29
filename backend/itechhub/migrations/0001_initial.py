# Generated by Django 5.0 on 2023-12-15 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('career_summary', models.JSONField(default=dict)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_images', to='common.image')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

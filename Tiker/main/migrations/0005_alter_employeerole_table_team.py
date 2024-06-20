# Generated by Django 5.0.6 on 2024-06-15 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_department'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employeerole',
            table='DimEmployeeType',
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.CharField(max_length=256)),
                ('DepartmentId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.department')),
            ],
            options={
                'db_table': 'DimTeam',
            },
        ),
    ]

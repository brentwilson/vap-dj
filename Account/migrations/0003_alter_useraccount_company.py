# Generated by Django 5.1.1 on 2024-09-22 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_useraccount_options_alter_useraccount_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.company'),
        ),
    ]

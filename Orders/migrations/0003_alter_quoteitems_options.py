# Generated by Django 5.1.1 on 2024-09-23 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_quote_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quoteitems',
            options={'ordering': ['list_order'], 'verbose_name_plural': 'Quote Items'},
        ),
    ]

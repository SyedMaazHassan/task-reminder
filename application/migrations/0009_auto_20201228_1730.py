# Generated by Django 3.1.4 on 2020-12-28 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20201228_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_type',
            old_name='name',
            new_name='system_name',
        ),
    ]

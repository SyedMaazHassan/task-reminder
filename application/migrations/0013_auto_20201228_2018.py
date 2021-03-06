# Generated by Django 3.1.4 on 2020-12-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20201228_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_type',
            name='pin_color',
            field=models.CharField(choices=[('Backup battery', 'Green'), ('Locking System', 'Blue'), ('Dim generator', 'Black'), ('Alarm System', 'Purple'), ('Access control system', 'Orange'), ('Door automation', 'Dark Purple')], max_length=50),
        ),
        migrations.AlterField(
            model_name='service_type',
            name='system_name',
            field=models.CharField(choices=[('Backup battery', 'Green'), ('Locking System', 'Blue'), ('Dim generator', 'Black'), ('Alarm System', 'Purple'), ('Access control system', 'Orange'), ('Door automation', 'Dark Purple')], max_length=50),
        ),
    ]

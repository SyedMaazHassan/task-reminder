# Generated by Django 3.1.4 on 2020-12-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20201228_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_type',
            name='pin_color',
            field=models.CharField(choices=[('Purple', 'Alarm System'), ('Blue', 'Locking System'), ('Dark Purple', 'Door automation'), ('Black', 'Dim generator'), ('Green', 'Backup battery'), ('Orange', 'Access control system')], max_length=20),
        ),
    ]

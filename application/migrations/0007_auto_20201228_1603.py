# Generated by Django 3.1.4 on 2020-12-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_customerinfo_geoinfo_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='qrcode',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

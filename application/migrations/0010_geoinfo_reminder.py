# Generated by Django 3.1.4 on 2020-12-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20201228_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoinfo',
            name='reminder',
            field=models.BooleanField(default=False),
        ),
    ]

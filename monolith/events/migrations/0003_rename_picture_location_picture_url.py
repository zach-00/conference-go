# Generated by Django 4.0.3 on 2023-11-27 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='picture',
            new_name='picture_url',
        ),
    ]

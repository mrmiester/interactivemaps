# Generated by Django 2.2 on 2020-03-19 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0015_auto_20200319_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='images',
            new_name='file',
        ),
    ]

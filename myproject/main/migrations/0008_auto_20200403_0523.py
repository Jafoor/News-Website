# Generated by Django 3.0.4 on 2020-04-03 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200311_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='site_set',
            new_name='link',
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200330_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='shor_txt',
            new_name='short_txt',
        ),
    ]

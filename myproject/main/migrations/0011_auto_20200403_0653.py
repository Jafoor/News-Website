# Generated by Django 3.0.4 on 2020-04-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200403_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200310_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.TextField(default='-'),
        ),
    ]

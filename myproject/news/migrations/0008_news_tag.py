# Generated by Django 3.0.4 on 2020-04-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200401_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
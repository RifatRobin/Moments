# Generated by Django 3.1.3 on 2021-01-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory_of_moments', '0003_auto_20210119_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moments',
            name='dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
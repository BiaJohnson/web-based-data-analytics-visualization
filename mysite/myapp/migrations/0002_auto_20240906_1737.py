# Generated by Django 3.2 on 2024-09-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='expenses_monthly',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='income_monthly',
            field=models.IntegerField(default=0),
        ),
    ]

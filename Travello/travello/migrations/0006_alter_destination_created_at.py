# Generated by Django 3.2.13 on 2022-04-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20220427_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-04-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_alter_destination_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/pics/'),
        ),
    ]
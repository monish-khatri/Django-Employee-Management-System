# Generated by Django 3.2.13 on 2022-04-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='employee/NoImage.png', upload_to='employee/'),
        ),
    ]

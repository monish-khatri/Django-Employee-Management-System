# Generated by Django 3.2.13 on 2022-05-10 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employeeteam'),
        ),
    ]
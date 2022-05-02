# Generated by Django 3.2.13 on 2022-05-02 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20220502_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Group', max_length=50)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'De-active')], default='1', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employeegroup'),
        ),
    ]
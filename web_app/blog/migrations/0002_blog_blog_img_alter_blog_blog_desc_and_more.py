# Generated by Django 4.0.4 on 2022-04-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(default='untitled.png', upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tags_blog_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='allow_to_add_comment',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.CharField(default='No', max_length=3),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=250)),
                ('tag_status', models.IntegerField(default='1')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tags',
            field=models.ManyToManyField(to='blog.tags'),
        ),
    ]

# Generated by Django 3.2 on 2021-06-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(default='', max_length=1500),
        ),
    ]

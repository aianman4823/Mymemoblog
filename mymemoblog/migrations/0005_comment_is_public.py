# Generated by Django 2.2.3 on 2019-07-12 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymemoblog', '0004_auto_20190712_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]

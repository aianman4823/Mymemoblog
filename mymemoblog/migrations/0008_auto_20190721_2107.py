# Generated by Django 2.2.3 on 2019-07-21 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymemoblog', '0007_auto_20190721_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_public',
            new_name='is_publick',
        ),
    ]

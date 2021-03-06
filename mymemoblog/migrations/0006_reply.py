# Generated by Django 2.2.3 on 2019-07-12 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymemoblog', '0005_comment_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField()),
                ('is_public', models.BooleanField(default=False)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymemoblog.Comment')),
            ],
        ),
    ]

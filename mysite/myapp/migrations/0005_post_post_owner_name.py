# Generated by Django 3.1.3 on 2020-11-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201121_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_owner_name',
            field=models.CharField(blank=True, default='Person', max_length=200, null=True),
        ),
    ]

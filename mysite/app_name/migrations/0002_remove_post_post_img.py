# Generated by Django 3.1.3 on 2020-11-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_img',
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-21 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.person'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sessionplayer',
            name='attendance',
            field=models.BooleanField(null=True),
        ),
    ]

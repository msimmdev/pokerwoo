# Generated by Django 3.0.6 on 2020-06-15 02:41

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=upload.models.upload_path)),
            ],
        ),
    ]

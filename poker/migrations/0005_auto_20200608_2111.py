# Generated by Django 3.0.6 on 2020-06-08 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0004_auto_20200601_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameparticipant',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='poker.Game'),
        ),
        migrations.AlterField(
            model_name='table',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='poker.Game'),
        ),
        migrations.AlterField(
            model_name='tableparticipant',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='poker.Table'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-06-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0004_auto_20200621_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='gain_per_game',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stats',
            name='place_rate',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stats',
            name='win_rate',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stats',
            name='average_placing',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stats',
            name='average_rating',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]

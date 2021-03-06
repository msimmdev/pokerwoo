# Generated by Django 3.0.6 on 2020-06-15 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pokerth_name', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.URLField(blank=True, null=True)),
                ('payment_link', models.URLField(blank=True, null=True)),
                ('payment_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('bank_sort_code', models.CharField(blank=True, max_length=6, null=True)),
                ('active', models.BooleanField(blank=True, default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentObligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_ref', models.PositiveIntegerField(default=0)),
                ('payment_amount', models.PositiveIntegerField(default=0)),
                ('payment_sent', models.BooleanField(blank=True, default=False)),
                ('payment_confirmed', models.BooleanField(blank=True, default=False)),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='players.Player')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='players.Player')),
            ],
        ),
    ]

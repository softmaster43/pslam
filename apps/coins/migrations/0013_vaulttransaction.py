# Generated by Django 2.0.2 on 2018-03-12 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coins', '0012_auto_20180312_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaultTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('balance', models.CharField(blank=True, max_length=20)),
                ('currency', models.CharField(blank=True, max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=200)),
                ('transaction_to', models.CharField(blank=True, max_length=200)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
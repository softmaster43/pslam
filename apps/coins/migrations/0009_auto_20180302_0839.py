# Generated by Django 2.0.2 on 2018-03-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0008_auto_20180302_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaultwallet',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='vaultwallet',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='vaultwallet',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='vaultwallet',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='vaultwallet',
            name='transaction_to',
        ),
        migrations.AddField(
            model_name='vaultwallet',
            name='addresses',
            field=models.ManyToManyField(to='coins.WalletAddress'),
        ),
        migrations.AddField(
            model_name='vaultwallet',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='vaultwallet',
            name='private',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='vaultwallet',
            name='public',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='vaultwallet',
            name='words',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
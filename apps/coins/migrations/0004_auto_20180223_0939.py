# Generated by Django 2.0.2 on 2018-02-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_transaction_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='address',
        ),
        migrations.AddField(
            model_name='wallet',
            name='addresses',
            field=models.ManyToManyField(to='coins.WalletAddress'),
        ),
    ]

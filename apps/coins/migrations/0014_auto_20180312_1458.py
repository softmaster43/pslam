# Generated by Django 2.0.2 on 2018-03-12 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0013_vaulttransaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaulttransaction',
            old_name='username',
            new_name='user',
        ),
    ]
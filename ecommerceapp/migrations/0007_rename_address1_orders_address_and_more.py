# Generated by Django 5.1.6 on 2025-02-28 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0006_remove_orderupdate_delivered_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
    ]

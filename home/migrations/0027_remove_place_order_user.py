# Generated by Django 4.0.3 on 2022-04-14 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_place_order_collect_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place_order',
            name='user',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_place_order_user_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place_order',
            name='collect_by_user',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

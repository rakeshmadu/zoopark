# Generated by Django 2.2.3 on 2019-08-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0004_auto_20190822_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30),
        ),
    ]

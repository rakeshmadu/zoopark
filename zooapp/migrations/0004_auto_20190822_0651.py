# Generated by Django 2.2.3 on 2019-08-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0003_auto_20190822_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('transgender', 'transgender')], max_length=30),
        ),
    ]

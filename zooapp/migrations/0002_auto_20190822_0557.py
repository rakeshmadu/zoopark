# Generated by Django 2.2.3 on 2019-08-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='age',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='contact_number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='country',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='pincode',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='state',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

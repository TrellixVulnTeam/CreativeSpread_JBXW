# Generated by Django 3.0.1 on 2019-12-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativewriting', '0002_auto_20191227_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='description',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
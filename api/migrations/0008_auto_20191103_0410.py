# Generated by Django 2.1.3 on 2019-11-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191102_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='details',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='audio',
            name='tags',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='url',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]

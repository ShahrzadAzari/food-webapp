# Generated by Django 2.2.5 on 2019-10-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_remove_foods_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='time',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

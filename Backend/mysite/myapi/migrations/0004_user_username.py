# Generated by Django 3.0.7 on 2020-06-18 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200616_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]

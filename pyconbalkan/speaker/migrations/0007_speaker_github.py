# Generated by Django 2.0.5 on 2018-06-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0006_auto_20180610_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0009_remove_conference_timetable_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='conference_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

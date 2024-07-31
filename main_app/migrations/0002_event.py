# Generated by Django 5.0.7 on 2024-07-31 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='Date & Time')),
                ('room_area', models.CharField(max_length=100)),
                ('attendees', models.IntegerField()),
                ('performances', models.CharField(max_length=100)),
            ],
        ),
    ]

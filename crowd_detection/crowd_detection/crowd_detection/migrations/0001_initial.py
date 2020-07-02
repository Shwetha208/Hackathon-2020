# Generated by Django 3.0.5 on 2020-04-14 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(default=None, max_length=100)),
                ('latitude', models.CharField(default=None, max_length=100)),
                ('longitude', models.CharField(default=None, max_length=100)),
                ('is_occupied', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(default=None, max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowd_detection.MapLocation')),
            ],
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_key', models.CharField(max_length=255, unique=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WellData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_well_number', models.CharField(max_length=20)),
                ('oil', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('brine', models.IntegerField()),
            ],
        ),
    ]

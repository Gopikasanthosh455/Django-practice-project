# Generated by Django 5.1.4 on 2024-12-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile_number', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Address', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Course', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Institute', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Course_duration', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
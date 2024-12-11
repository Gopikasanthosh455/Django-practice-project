# Generated by Django 5.1.4 on 2024-12-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LumApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Duration', models.CharField(blank=True, max_length=100, null=True)),
                ('Fees', models.IntegerField(blank=True, null=True)),
                ('Institute', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_alter_studentdb_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdb',
            name='Course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='Course_duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='Institute',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

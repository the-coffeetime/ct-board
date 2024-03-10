# Generated by Django 5.0.2 on 2024-03-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobCreationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.PositiveBigIntegerField(db_column='userID')),
                ('fieldName', models.CharField(db_column='fieldName', max_length=255)),
                ('jobName', models.CharField(db_column='jobName', max_length=255)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'jobCreationRequest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('jobID', models.AutoField(db_column='jobID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'jobs',
                'managed': False,
            },
        ),
    ]
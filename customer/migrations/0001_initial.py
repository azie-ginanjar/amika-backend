# Generated by Django 3.0.5 on 2020-04-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('districts', models.CharField(max_length=35)),
                ('zip_code', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]

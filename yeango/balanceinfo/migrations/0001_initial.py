# Generated by Django 2.0.1 on 2018-01-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Knight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sir_name', models.CharField(max_length=100)),
                ('public_api', models.CharField(max_length=50)),
                ('secret_api', models.CharField(max_length=50)),
            ],
        ),
    ]

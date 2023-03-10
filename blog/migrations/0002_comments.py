# Generated by Django 2.2.5 on 2019-10-09 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='comments/')),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

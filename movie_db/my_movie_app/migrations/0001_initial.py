# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('time_stamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('release_date', models.CharField(max_length=30)),
                ('video_release_date', models.CharField(max_length=30)),
                ('imdb_url', models.CharField(max_length=200)),
                ('unknown', models.BooleanField()),
                ('action', models.BooleanField()),
                ('adventure', models.BooleanField()),
                ('animation', models.BooleanField()),
                ('childrens', models.BooleanField()),
                ('comedy', models.BooleanField()),
                ('crime', models.BooleanField()),
                ('documentary', models.BooleanField()),
                ('drama', models.BooleanField()),
                ('fantasy', models.BooleanField()),
                ('film_noir', models.BooleanField()),
                ('horror', models.BooleanField()),
                ('musical', models.BooleanField()),
                ('mystery', models.BooleanField()),
                ('romance', models.BooleanField()),
                ('sci_fi', models.BooleanField()),
                ('thriller', models.BooleanField()),
                ('war', models.BooleanField()),
                ('western', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_movie_app.Item'),
        ),
        migrations.AddField(
            model_name='data',
            name='rater_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_movie_app.Rater'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=255, default='demoUser')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('text', models.TextField(null=True)),
                ('quote', models.TextField(null=True)),
                ('ranges_start', models.CharField(max_length=255, null=True)),
                ('ranges_end', models.CharField(max_length=255, null=True)),
                ('ranges_start_offset', models.IntegerField(null=True)),
                ('ranges_end_offset', models.IntegerField(null=True)),
                ('tags', models.TextField(default='[]')),
                ('permissions_read', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('number', models.IntegerField(default=0)),
                ('stage', models.IntegerField(default=0)),
                ('origin', models.CharField(max_length=255, default='null')),
                ('last_action', models.CharField(max_length=255, default='null')),
                ('caption_version', models.CharField(max_length=255, default='null')),
                ('caption_text', models.TextField(default='null')),
                ('coauthors', models.CharField(max_length=255, default='null')),
                ('sponsors', models.CharField(max_length=255, default='null')),
                ('cosponsors', models.CharField(max_length=255, default='null')),
                ('subjects', models.TextField(default='null')),
                ('authors', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('annotation', models.ForeignKey(to='annotation_app.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('committee', models.CharField(max_length=255)),
                ('is_chair', models.BooleanField()),
                ('bills', models.ManyToManyField(to='annotation_app.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('bills', models.ManyToManyField(to='annotation_app.Bill')),
            ],
        ),
        migrations.AddField(
            model_name='annotation',
            name='bill',
            field=models.ForeignKey(to='annotation_app.Bill'),
        ),
    ]

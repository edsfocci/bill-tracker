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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user', models.CharField(max_length=255, default='demoUser')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('text', models.TextField(null=True)),
                ('quote', models.TextField(null=True)),
                ('ranges_start', models.CharField(null=True, max_length=255)),
                ('ranges_end', models.CharField(null=True, max_length=255)),
                ('ranges_start_offset', models.IntegerField(null=True)),
                ('ranges_end_offset', models.IntegerField(null=True)),
                ('tags', models.TextField(default='[]')),
                ('permissions_read', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('session', models.CharField(max_length=3)),
                ('chamber_origin', models.CharField(max_length=1)),
                ('number', models.IntegerField()),
                ('text', models.TextField()),
                ('authors', models.TextField(null=True)),
                ('subjects', models.TextField(null=True)),
                ('stage', models.IntegerField(null=True)),
                ('last_action', models.CharField(null=True, max_length=255)),
                ('caption_version', models.CharField(null=True, max_length=255)),
                ('caption_text', models.TextField(null=True)),
                ('coauthors', models.CharField(null=True, max_length=255)),
                ('sponsors', models.CharField(null=True, max_length=255)),
                ('cosponsors', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('annotation', models.ForeignKey(to='annotation_app.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('committee', models.CharField(null=True, max_length=255)),
                ('is_chair', models.BooleanField(default=False)),
                ('bills', models.ManyToManyField(to='annotation_app.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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

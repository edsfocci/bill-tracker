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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('session', models.CharField(max_length=3)),
                ('chamber_origin', models.CharField(max_length=1)),
                ('number', models.IntegerField()),
                ('text', models.TextField()),
                ('authors', models.TextField(null=True)),
                ('subjects', models.TextField(null=True)),
                ('stage', models.IntegerField(null=True)),
                ('last_action', models.CharField(max_length=255, null=True)),
                ('caption_version', models.CharField(max_length=255, null=True)),
                ('caption_text', models.TextField(null=True)),
                ('coauthors', models.CharField(max_length=255, null=True)),
                ('sponsors', models.CharField(max_length=255, null=True)),
                ('cosponsors', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('annotation', models.ForeignKey(to='annotation_app.Annotation')),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('committee', models.CharField(max_length=255, null=True)),
                ('is_chair', models.BooleanField(default=False)),
                ('bills', models.ManyToManyField(to='annotation_app.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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

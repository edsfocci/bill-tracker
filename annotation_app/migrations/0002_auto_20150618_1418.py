# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('committee', models.CharField(max_length=255)),
                ('is_chair', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='annotation',
            old_name='reporter',
            new_name='bill',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='reporter',
            new_name='annotation',
        ),
        migrations.AddField(
            model_name='annotation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='permissions_read',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='annotation',
            name='quote',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='ranges_end_offset',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='ranges_start_offset',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='tags',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='user',
            field=models.CharField(max_length=255, default='demoUser'),
        ),
        migrations.AddField(
            model_name='bill',
            name='authors',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='caption_text',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='caption_version',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='coauthors',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='cosponsors',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='last_action',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='origin',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='sponsors',
            field=models.CharField(max_length=255, default='null'),
        ),
        migrations.AddField(
            model_name='bill',
            name='stage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='subjects',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='bills',
            field=models.ManyToManyField(to='annotation_app.Bill'),
        ),
        migrations.AddField(
            model_name='senator',
            name='bills',
            field=models.ManyToManyField(to='annotation_app.Bill'),
        ),
    ]

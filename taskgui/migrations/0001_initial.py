# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-09 19:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='checkup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stamp', models.DateTimeField()),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='context',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stamp', models.DateTimeField()),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField(null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.note')),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('due', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('overview', models.TextField(null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('storage', models.CharField(blank=True, max_length=100, null=True)),
                ('priority', models.IntegerField(null=True)),
                ('context', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.context')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.task')),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_by', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.role')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.status')),
            ],
        ),
        migrations.CreateModel(
            name='ttype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_pref',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100)),
                ('value', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='ttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskgui.ttype'),
        ),
        migrations.AddField(
            model_name='note',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.task'),
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.note'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checkup',
            name='note_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.task'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskgui', '0002_auto_20161111_2321'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tag',
        ),
        migrations.RemoveField(
            model_name='task',
            name='context',
        ),
        migrations.RemoveField(
            model_name='task',
            name='role',
        ),
        migrations.AddField(
            model_name='task',
            name='for_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='for_dept', to='taskgui.department'),
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='w_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='w_dept', to='taskgui.department'),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.DeleteModel(
            name='context',
        ),
        migrations.DeleteModel(
            name='role',
        ),
        migrations.AddField(
            model_name='task',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskgui.location'),
        ),
    ]
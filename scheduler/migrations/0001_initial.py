# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('function_name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('args', models.TextField(blank=True, null=True)),
                ('kwargs', models.TextField(blank=True, null=True)),
                ('rrule', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('running', 'Running'), ('success', 'Success'), ('failure', 'Failure'), ('cancelled', 'Cancelled')], default='created', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledTaskRunLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.ScheduledTask')),
            ],
        ),
    ]

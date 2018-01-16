# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:45
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
            name='Analyzer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Analyzer name')),
            ],
        ),
        migrations.CreateModel(
            name='Decay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decay_time', models.FloatField()),
                ('event_time', models.DateTimeField()),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Analyzer')),
            ],
        ),
        migrations.CreateModel(
            name='Pulse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pulse_width_ch0', models.FloatField()),
                ('pulse_width_ch1', models.FloatField()),
                ('pulse_width_ch2', models.FloatField()),
                ('pulse_width_ch3', models.FloatField()),
                ('event_time', models.DateTimeField()),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Analyzer')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_ch0', models.FloatField()),
                ('rate_ch1', models.FloatField()),
                ('rate_ch2', models.FloatField()),
                ('rate_ch3', models.FloatField()),
                ('rate_cht', models.FloatField()),
                ('time_window', models.FloatField()),
                ('query_time', models.DateTimeField()),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Analyzer')),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('run_id', models.UUIDField(primary_key=True, serialize=False)),
                ('simulation', models.BooleanField(default=False)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Velocity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_time', models.FloatField()),
                ('event_time', models.DateTimeField()),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Analyzer')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Run')),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Run'),
        ),
        migrations.AddField(
            model_name='pulse',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Run'),
        ),
        migrations.AddField(
            model_name='decay',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muonic_django.Run'),
        ),
    ]

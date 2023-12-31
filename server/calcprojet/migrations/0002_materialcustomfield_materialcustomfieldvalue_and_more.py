# Generated by Django 5.0 on 2023-12-11 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcprojet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCustomField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCustomFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NeedRessource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NeedType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='created_by_email',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('exclude_from_storage', models.BooleanField(default=False)),
                ('capacity_factor', models.FloatField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcprojet.project')),
                ('needs_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcprojet.needtype')),
            ],
        ),
        migrations.CreateModel(
            name='NeedValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('hour_start', models.DateTimeField(blank=True)),
                ('hour_end', models.DateTimeField(blank=True)),
                ('day_start', models.IntegerField(blank=True)),
                ('day_end', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcprojet.need')),
            ],
        ),
    ]

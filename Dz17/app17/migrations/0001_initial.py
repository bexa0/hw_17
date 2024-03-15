# Generated by Django 5.0.1 on 2024-03-05 10:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('1', 'высокий'), ('2', 'средний'), ('3', 'низкий')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='in process', max_length=255)),
                ('completed_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('made_at', models.DateTimeField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app17.actiontype')),
            ],
        ),
    ]
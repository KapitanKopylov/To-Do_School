# Generated by Django 4.1.5 on 2023-03-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('device_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=None, max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('item_id', models.CharField(default=None, max_length=200)),
                ('mail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TodoUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('location', models.CharField(max_length=120)),
                ('publication_date', models.DateField()),
                ('activate', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updeted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
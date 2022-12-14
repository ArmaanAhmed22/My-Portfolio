# Generated by Django 4.0.6 on 2022-07-23 13:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_cvitemlistexpandible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvitemlistexpandible',
            name='expand',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]

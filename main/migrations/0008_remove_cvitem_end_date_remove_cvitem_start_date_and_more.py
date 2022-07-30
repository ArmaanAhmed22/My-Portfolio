# Generated by Django 4.0.6 on 2022-07-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cvcategory_cvitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvitem',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='cvitem',
            name='start_date',
        ),
        migrations.AddField(
            model_name='cvitem',
            name='end_month',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='cvitem',
            name='end_year',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='cvitem',
            name='start_month',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='cvitem',
            name='start_year',
            field=models.IntegerField(default=-1),
        ),
    ]
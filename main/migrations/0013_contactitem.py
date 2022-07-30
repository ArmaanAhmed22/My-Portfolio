# Generated by Django 4.0.6 on 2022-07-29 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_cvitemlistexpandible_expand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sender_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('contact_time', models.DateTimeField()),
                ('send_status', models.BooleanField(default=0)),
            ],
        ),
    ]
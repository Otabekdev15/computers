# Generated by Django 4.1.6 on 2023-03-03 03:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Comment',
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-24 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_users', '0011_user_first_name_150_max_length'),
        ('openwisp_ipam', '0003_shareable_subnets'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subnet', unique_together={('subnet', 'organization')},
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_image_post_b_post_image_post_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='IMAGE_POST_B',
        ),
        migrations.RemoveField(
            model_name='post',
            name='IMAGE_POST_C',
        ),
    ]

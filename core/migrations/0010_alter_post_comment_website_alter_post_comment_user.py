# Generated by Django 4.2.1 on 2023-05-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_post_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='Website',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_comment',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='post_comment',
            old_name='Name',
            new_name='user',
        ),
        migrations.AddField(
            model_name='post_comment',
            name='parent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.post_comment'),
        ),
        migrations.AddField(
            model_name='post_comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
    ]

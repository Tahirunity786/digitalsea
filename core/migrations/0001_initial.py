# Generated by Django 4.2.1 on 2023-05-19 14:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('slug', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Phone_no', models.IntegerField(default='0')),
                ('User_Subject', models.CharField(default='', max_length=500)),
                ('Comment', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feature_Image', models.ImageField(default='default_image.jpg', upload_to='Post')),
                ('Title', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=100)),
                ('Date', models.DateField(auto_now_add=True, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('new_slug', models.CharField(max_length=100, null=True, unique=True)),
                ('Draft', models.BooleanField(null=True)),
                ('Publish', models.BooleanField(blank=True, null=True)),
                ('section', models.CharField(blank=True, choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Trending', 'Trending'), ('Recomended', 'Recomended'), ('Inspirations', 'Inspirations'), ('Latest_Post', 'Latest_Post')], default='', max_length=200)),
                ('Main_Post', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Website', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('User_Message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
        ),
    ]

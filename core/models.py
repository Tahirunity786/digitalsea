from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils.timezone import now 


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200, default='')
    slug = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.Name

    # def image_tag1(self):
    #     return format_html(

    
class Contact(models.Model):
    Username = models.CharField(max_length=100, default='')
    Email = models.CharField(max_length=50, default='')
    Phone_no = models.IntegerField(default='0')
    User_Subject = models.CharField(max_length=500, default='')
    Comment = models.TextField()
    Date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    

class Tag(models.Model):
    Name = models.CharField(max_length=100, default='')
    post = models.ForeignKey('Post', related_name='tags', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name


class Post(models.Model):
    SECTION = (
        ('Popular', 'Popular'),
        ('Recent', 'Recent'),
        ('Trending', 'Trending'),
        ('Recommended', 'Recommended'),
        ('Inspirations', 'Inspirations'),
        ('Latest_Post', 'Latest_Post'),
    )

    Feature_Image = models.ImageField(upload_to='Post', default='default_image.jpg')
    Title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True, null=True, blank=True)
    content = RichTextField()
    new_slug = models.CharField(max_length=100, unique=True, null=True)
    Draft = models.BooleanField(null=True)
    Publish = models.BooleanField(null=True, blank=True)
    section = models.CharField(choices=SECTION, max_length=200, default='', blank=True)
    Main_Post = models.BooleanField()


    def __str__(self):
        return self.Title

    def profile_image(self):
        return format_html(
            '<img src="/media/{}" style="height:60px; width:60px;border-radius:50%;" />'.format(self.Feature_Image))


class Post_comment(models.Model):
    Date = models.DateTimeField(default=now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, blank=True)
    user = models.CharField(max_length=100, default='', null=True)
    email = models.CharField(max_length=50, default='')
    Website = models.CharField(max_length=100, default='', null=True, blank=True)
    User_Message = models.TextField(default='')

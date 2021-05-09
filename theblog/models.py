from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       # return reverse('article-detail',args=(str(self.id)))
       return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):


    def get_absolute_url(self):
       # return reverse('article-detail',args=(str(self.id)))
       return reverse('home')

    def get_profile_picture(self):
        if self.profile_picture:
            return profile_picture_url
        else:
            return 'your_default_img_url_path'    


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =  RichTextField(blank=True, null=True)
    #body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippets = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    

    def total_likes(self):
        self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
       # return reverse('article-detail',args=(str(self.id)))
       return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s-%s' %(self.post.title, self.name)
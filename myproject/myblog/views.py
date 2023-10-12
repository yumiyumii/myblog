from django.shortcuts import render
from django.db import models

# Create your views here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_passwrord = models.CharField(max_length=20)
    user_pic= models.CharField(max_length=20)
    user_nickname= models.CharField(max_length=20)

class Category(models.Model):
    DAILY = 0
    COOKING=1
    TRAVEL=2
    MOVIE =3
    IT =4
    BOOK =5
    LIVING =6
    FASHION =7
    

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    upload_file = models.FileField(upload_to='blog/')
    user_nickname= models.CharField(max_length=20)
    like_cnt = models.IntegerField(default=0, null=True)

class Comment(models.Model):
    user_id = models.CharField(max_length=20)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    comt_upload_date = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField(default=0, null=True)





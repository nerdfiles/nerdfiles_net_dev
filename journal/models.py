from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('Date published')

class Comment(models.Model):
  post = models.ForeignKey(Post)
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('Date published')
  like = models.IntegerField()
    
class Page(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('Date published')

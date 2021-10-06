from django.db import models
from django_quill.fields import QuillField
from django.db.models.fields import CharField
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = QuillField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def comments(self):
        return self.comment_set.all()
    
    

class Comment(models.Model):
    name = CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.user.username 

    
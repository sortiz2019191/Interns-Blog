from django.contrib import admin

from .models import Post, Comment, PostView

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
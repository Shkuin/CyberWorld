from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    preview_text = models.CharField(max_length=150)
    text = HTMLField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)
    preview_image = models.ImageField(upload_to='static/img')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # это называется url-реверсинг

    def __str__(self):
        return '{}'.format(self.title)


class Player(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="android.png", null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = HTMLField()
    create = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))

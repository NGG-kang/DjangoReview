from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d", blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post_set", blank=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



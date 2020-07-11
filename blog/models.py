from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    topic = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='media/upload/%Y/%m/%d/')
    published = models.BooleanField(default=False)
    content = RichTextUploadingField()

    def __str__(self):
        return self.topic

    def published_year(self):
        return self.pub_date.strftime('%Y')

    def published_month(self):
        return self.pub_date.strftime('%m')

    class Meta:
        ordering = ('-pub_date',)


class PostTag(models.Model):
    tag = models.TextField()
    posts = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
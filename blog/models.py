from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    topic = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('-pub_date',)

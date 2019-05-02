from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    topic = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('-pub_date',)

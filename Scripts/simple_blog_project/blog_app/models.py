from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogArtcle(models.Model):
    title=models.CharField(primary_key=True, max_length=400)
    blog_content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


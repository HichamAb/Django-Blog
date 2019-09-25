from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify
import uuid
# Create your models here.


class BlogPost(models.Model):
    title=models.CharField(max_length=255,null=False)
    content=models.TextField(null=False)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(default=uuid.uuid1,max_length=255,unique=True)#slug to use it on the url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
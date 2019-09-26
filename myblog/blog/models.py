from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify
import uuid
from PIL import Image
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

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile.jpg',upload_to="profile_pics")

    def __str__(self):
        return "{}'s Profile".format(self.user.username)
    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
from django.db import models
from PIL import Image

# Create your models here.

class loveclass(models.Model):

    lovecate = models.CharField(max_length=100,unique=True)
    loveimg = models.ImageField(upload_to='lover/%Y%m%d/', blank=True)
    songer_id = models.IntegerField(default=0)

    def save(self,*args,**kwargs):

        article = super(loveclass, self).save(*args, **kwargs)

        if self.loveimg and not kwargs.get('update_fields'):
            image = Image.open(self.loveimg)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.loveimg.path)
        return article



class songer(models.Model):

    songername = models.CharField(max_length=100)
    musicname = models.CharField(max_length=100)
    songid = models.IntegerField(default=1024)


class songcomment(models.Model):

    comment_id = models.IntegerField()
    songname = models.CharField(max_length=100)
    commenter = models.CharField(max_length=100)
    comment = models.TextField()
    likedcount = models.IntegerField(default=0)
    avatarurl = models.CharField(max_length=512)
    comment_time = models.DateTimeField()



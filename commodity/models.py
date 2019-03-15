from django.db import models
from django.utils import timezone

# Create your models here.


class commonDity(models.Model):
    commonName = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    commonNum = models.IntegerField(default=0)
    update_time = models.DateTimeField(default=timezone.now,verbose_name='更新时间')

    class Meta:
        verbose_name = '商品信息'
        ordering = ['-commonNum']
        db_table = 'commondity'


class shopname(models.Model):

    shop_name = models.CharField(max_length=100,default='null')
    common_id = models.IntegerField()
    commonNum = models.IntegerField()
    commonName = models.CharField(max_length=100,default='null')
    platform = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    shopurl = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name = '店家信息'
        ordering = ['-commonNum']
        db_table = 'shopname'

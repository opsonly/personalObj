from django.db import models
from mdeditor.fields import MDTextField #必须导入
from django.conf import settings

from django.utils import timezone
# Create your models here.

class bloglist(models.Model):

    name = models.CharField(max_length=100)
    total_views = models.PositiveIntegerField(default=0)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,to_field='username',default='xiaoshui',on_delete='null')
    category = models.CharField(max_length=50,blank=True)
    content = MDTextField()
    commit = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name


    class Meta:
        verbose_name = '博客信息'
        ordering = ['-update_time']
        db_table = 'bloglist'
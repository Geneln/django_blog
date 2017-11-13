from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    #分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #标题
    title = models.CharField(max_length=70)
    #正文
    body = models.TextField()

    #创建和最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要,可有可无
    excerpt = models.CharField(max_length=200,blank=True)

    #外键,一篇文章可以有多个分类(一对多),多个标签可能有多个文章(多对多)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    #文章作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


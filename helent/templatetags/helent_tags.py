#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import template
from ..models import Post, Category

register = template.Library()


# 最新文章标签(5篇)
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模版标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模版标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

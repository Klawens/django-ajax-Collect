# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from register.models import UserInfo
# Create your models here.


class UserFavorite(models.Model):
	FAV_TYPE_CHOICES = [
		('animal', 1),
		('post', 2),
		('station', 3),
	]
	#这里定义了三种收藏类型
	user = models.ForeignKey(UserInfo, verbose_name=u"用户")#外键连接用户表，这里叫UserIfo
	fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")#收藏对象id
	fav_type = models.CharField(max_length=10, choices=FAV_TYPE_CHOICES, verbose_name=u"收藏类型")

	class Meta:
		verbose_name = u"用户收藏"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.user.username
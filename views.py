# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from operation.models import UserFavorite   #models位置


class CollectView(View):

	def post(self, request):
		#在ajax那获取两个值
		fav_id = request.POST.get('fav_id', '0')
		fav_type = request.POST.get('fav_type', '')

		#判断用户是否登录
		if not request.user.is_authenticated:
			info = {'status':'fail', 'msg':'未登录'}
			return JsonResponse(info, safe=False)
			#未登录，ajax控制页面跳转

		exist_record = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
		#查找是否存在收藏记录

		#如果存在
		if exist_record:
			exist_record.delete()
			info = {'status':'fail', 'msg':'&hearts;&nbsp;收藏'}
			return JsonResponse(info, safe=False)
		#如果不存在
		else:
			user_fav = UserFavorite()
			#判断参数正常，这里可以int(fav_id)确保数据类型
			if (fav_id > 0) and fav_type:
				user_fav.fav_id = fav_id
				user_fav.fav_type = fav_type
				user_fav.user = request.user
				user_fav.save()
				info = {'status':'success', 'msg':'已收藏'}
				return JsonResponse(info, safe=False)
			else:
				info = {'status':'fail', 'msg':'收藏失败'}
				return JsonResponse(info, safe=False)

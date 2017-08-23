# -*- coding: utf-8 -*-

from django.conf.urls import url

from community.views import CollectView


urlpatterns = [
	url(r'^fav/$', CollectView.as_view(), name='favorite'),
]
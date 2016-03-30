# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from search.es_access import query


class ListMedia(APIView):
	renderer_classes = (JSONRenderer, )
	
	def get(self,request,format=None):
		if request:
			title = request.GET.get('title')
			if title:
				print query(title)
				return Response(query(title))
			else:
				return Response({"status":"failure","msg":"参数不能为空！"})
		else:
			return Response({"status":"failure","msg":"参数不能为空！"})
		








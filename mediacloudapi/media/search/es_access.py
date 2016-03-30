# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search,Q
from mediacloudapi.settings import LOG_FILE,ELASTICSEARCH
from mediacloudapi.media.models import McMediainfo
import json
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def query(es_filter):
	es_data=[]

	es_config=ELASTICSEARCH
	
	client = Elasticsearch(
		[{'host':es_config['HOST'],'port':es_config['PORT']}],
		sniffer_timeout = es_config['TIME_OUT']
	)

	search_dsl = Search(using = client, index = es_config['SEARCH_INDEX'])
	result = search_dsl.query("match", title= es_filter)
	
	response=result.execute()
	for hit in response:
		media = {}
		media['page_url'] = hit.page_url
		media['title'] = hit.title
		media['eName'] = hit.eName
		media['otherName'] = hit.otherName
		media['adaptor'] = hit.adaptor
		media['director'] = hit.director
		media['leader'] = hit.leader
		media['kind'] = hit.kind
		media['language'] = hit.language
		media['duration'] = hit.duration
		media['story'] = hit.story
		media['keyWord'] = hit.keyWord
		media['productPerson'] = hit.productPerson
		media['dubbing'] = hit.dubbing
		media['executiver'] = hit.executiver
		media['original'] = hit.original
		media['productColtd'] = hit.productColtd
		media['productionTime'] = hit.productionTime
		media['licence'] = hit.licence
		media['registration'] = hit.registration
		media['distributColtd'] = hit.distributColtd
		media['totalNumber'] = hit.totalNumber
		media['updateInfo'] = hit.updateInfo
		media['area'] = hit.area
		media['source'] = hit.source
		media['playTime'] = hit.playTime
		media['producer'] = hit.producer
		media['television'] = hit.television

		es_data.append(media)	
	
	write_file_content(LOG_FILE, json.dumps(es_data,ensure_ascii=False,indent=4), 'a+')
	return json.dumps(es_data, ensure_ascii=False,indent=4)
	#return es_data

def write_file_content(filepath, text, mode='w'):
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	file_object = open(filepath+date+'.log', mode)
	file_object.write(text)
	file_object.close()

def convert_to_dict(obj):
	'''把Object对象转换成Dict对象'''
	dict = {}
	dict.update(obj.__dict__)
	return dict














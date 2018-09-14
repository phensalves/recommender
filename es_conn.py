#!/usr/bin/python
#encoding: UTF-8

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

class ConnectEs(object):
	"""docstring for ConnectES"""
	def __init__(self, *args):

		print *args

	# def init_conn(index, doc_type, es_id):
	# 	es.get(index=index, doc_type=doc_type, id=es_id)['_source']
	# 	print es['interests_id']


# example
# es.get(index="user_preferences", doc_type="user_preferences", id=39038)['_source']
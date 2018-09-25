#!/usr/bin/python
#encoding: UTF-8

from datetime import datetime
from elasticsearch import Elasticsearch
import code
es = Elasticsearch()

class ConnectEs(object):
	"""docstring for ConnectES"""
	def __init__(*args):
		print args
		init_conn(index, doc_type, es_id)

	def init_conn(index, es_id):
		es.get(index=index, doc_type=index, id=es_id)['_source']
		es['interests_id']


# example
# es.get(index="user_preferences", doc_type="user_preferences", id=39038)['_source']
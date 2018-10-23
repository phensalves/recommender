# coding=utf-8
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from elasticsearch_dsl import Search


class PdhElasticsearch(object):
    def __init__(self, index_name, user_id):
        self.index_name = index_name
        self.user_id = user_id

        current_user = self.get_user_preferences(index_name, user_id)
        if current_user is not None: self.get_similar_users(index_name, current_user['interests'])

    def get_similar_users(self, index, user_preferences):
        print(user_preferences)

        connections.create_connection(hosts=['localhost:9200'])
        client = Elasticsearch()
        body = self.build_query_body(user_preferences)
        s = Search(using=client).index(index).from_dict(body)
        res = s.execute()

        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print(hit['_source'])

    def build_query_body(self, list):
        print "THIS IS LIST %s" % list

        body = {
          "query": {
            "function_score": {
              "boost_mode": "replace",
              "query": {
                "match_all": {}
              },
              "script_score": dict(script="_source['interests'].containsAll(" + str(list) + ") ? 1 : 0")
            }
          },
          "filter": {
            "terms": {
              "interests": list
            }
          }
        }

        return body

    def get_user_preferences(self, index_name, user_id):
        index_name = index_name
        user_id = user_id
        result = Elasticsearch().get(index=index_name, doc_type=index_name, id=user_id)

        if result is not None: return result['_source']

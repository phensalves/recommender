# coding=utf-8
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search


class PdhElasticsearch(object):
    def __init__(self, index_name, user_id):
        self.index_name = index_name
        self.user_id = user_id

    def get_similar_users(self, index, user_preferences):
        connections.create_connection(hosts=['localhost:9200'])
        client = Elasticsearch()
        body = self.build_query_body(user_preferences)
        s = Search(using=client).index(index).from_dict(body)
        res = s.execute()

        print("Got %d Hits" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print(hit['_source'])
        if res is not None: return res['hits']['hits']

    def build_query_body(self, list):
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

    def get_elasticsearch_single_data(self, index_name, user_id):
        result = Elasticsearch().get(index=index_name, doc_type=index_name, id=user_id)

        if result is not None: return result['_source']

    def user_quality_ratings(self, user_id):
        result = self.get_elasticsearch_single_data('user_quality_ratings', user_id)

        if result is not None: return result['_source']
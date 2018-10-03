# coding=utf-8
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from elasticsearch_dsl import Search


class PdhElasticsearch():
    @classmethod
    def init_conn(cls, index_name, user_id):
        result = Elasticsearch().get(index=index_name, doc_type=index_name, id=user_id)

        if result is not None:
            return result['_source']

    def get_similar_users(self, index, user_preferences):
        connections.create_connection(hosts=['localhost:9200'])
        url = 'http://localhost:9200'
        client = Elasticsearch(url)
        s = Search(using=client)
        s = s.index(index)

        body = self.build_query_body(user_preferences)

        body = s.to_dict()

        res = s.execute()

        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print(hit["_source"])
    
    def build_query_body(self, list):
        body = {
            "query": {
                "function_score": {
                    "boost_mode": "replace",
                    "query": {
                        "match_all": {}
                    },
                    "script_score": {
                        "script": "_source['interests_ids'].containsAll(" + str(list) + ") ? 1 : 0"
                    }
                }
            },
            "size": 200000,
            "filter": {
                "terms": {
                    "interests_ids": list
                }
            }
        }

        return body

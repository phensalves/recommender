# coding=utf-8
from elasticsearch import Elasticsearch as es
from elasticsearch_dsl import Search as s
import numpy as np


class PdhElasticsearch():
    @classmethod
    def init_conn(self, index_name, user_id):
        result = es().get(index=index_name, doc_type=index_name, id=user_id)

        if result is not None:
            return result['_source']

    def get_similar_users(self, index, user_preferences, lat, lng):
        res = client.search(index="user_preferences", body={
            "query": {
                "function_score": {
                    "boost_mode": "replace",
                    "query": {"match_all": {}},
                    "script_score": {
                        "script": " _source['interests_ids_array'].containsAll(" + str([19, 20, 21, 22]) + ") ? "
                                                                                                      "2.3: "
                                                                                                      "0 "
                    }
                }
            }

        })

    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print(hit["_source"])

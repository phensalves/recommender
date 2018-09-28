from datetime import datetime
from elasticsearch import Elasticsearch as es


class PdhElasticsearch():
    @classmethod
    def init_conn(self, index_name, user_id):
        result = es().get(index=index_name, doc_type=index_name, id=user_id)

        if result is not None:
            return result['_source']

    def get_similar_users(self, user_preferences):
        res = es.search(index="test-index", body={"query": {
            "function_score": {
                "boost_mode": "replace",
                "query": {"match_all": {}},
                "script_score": {
                    "script": " _source['interests_ids_array'].containsAll( #{preferences} ) ? 2.3 : 0 "
                }
            }
        },
            "filter": {
                "bool": {
                    "must": [
                        {
                            "geo_distance": {
                                "distance": "50km",
                                "location": {
                                    "lat": "#{options[:lat]}",
                                    "lon": "#{options[:lon]}",
                                }
                            }
                        },
                        {
                            "terms": {
                                "interests_ids_array": preferences
                            }
                        }
                    ]
                }
            }
        })

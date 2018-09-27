from elasticsearch import Elasticsearch as es


class ConnectEs():
    @classmethod
    def init_conn(self, index_name, user_id):
        print 'entrou no init_conn'
        result = es().get(index=index_name, doc_type=index_name, id=user_id)
        if result > 0: print result

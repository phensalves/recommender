from elasticsearch import Elasticsearch as es


class ConnectEs():
    def __init__(self, index_name, user_id):
        print 'teeeeeest'
        init_conn(ConnectEs, index_name, user_id)


def init_conn(cls, index_name, user_id):
    print 'entrou no init_conn'
    result = es().get(index=index_name, doc_type=index_name, id=user_id)
    if result > 0: print result 

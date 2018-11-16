from elasticsearch import Elasticsearch
from config import ELASTICSEARCH


def create_client_elasticsearch(hosts=ELASTICSEARCH):
    return Elasticsearch(
        [hosts],
        scheme="http",
        port=80,
    )


# if __name__ == '__main__':
#     for i in range(200):
#         es = create_client_elasticsearch(
#             hosts=ELASTICSEARCH)
#         doc = {
#             'author': 'mineiro',
#             'text': 'Elasticsearch: funciona arrombado',
#             'timestamp': datetime.now(),
#         }
#         res = es.index(index="test-index", doc_type='tweet', id=i, body=doc)
#         print(res['result'])

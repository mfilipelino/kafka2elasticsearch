import elasticsearch_svc
import kafkaconsumer_svc
from base64 import b64decode
from elasticsearch.exceptions import RequestError
from config import BROKERS
from datetime import datetime
import json
import sys


def kafka2elasticsearch(topic, index):
    elastic_client = elasticsearch_svc.create_client_elasticsearch()
    consumer = kafkaconsumer_svc.create_kafka_consumer(topic=topic, group_id=index, bootstrap_servers=BROKERS)

    for msg in consumer:
        try:
            data = b64decode(msg.value.get('data'))
            dict_data = json.loads(data)
            dict_data.pop('order', None)
            dict_data.pop('properties', None)
            dict_data.pop('payload', None)
            init = datetime.now()
            res = elastic_client.index(index=index, doc_type='json', body=json.dumps(dict_data))
            end = datetime.now()
            print(end - init)
        except RequestError as request_error:
            print(request_error)
            print(data)
            raise request_error


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('python kafka2elasticsearch <topic> <index>')
        exit()

    kafka2elasticsearch(topic=sys.argv[1], index=sys.argv[2])

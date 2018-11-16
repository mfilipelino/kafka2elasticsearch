import elasticsearch_svc
import kafkaconsumer_svc

from base64 import b64decode
from elasticsearch.exceptions import RequestError
from config import BROKERS
import json
import sys
from multiprocessing.pool import Pool
from multiprocessing import cpu_count


def kafka2elasticsearch(topic, index, id):
    print('start process {}'.format(id))
    consumer = kafkaconsumer_svc.create_kafka_consumer(topic=topic, group_id=index, bootstrap_servers=BROKERS)
    client = elasticsearch_svc.create_client_elasticsearch()

    for msg in consumer:
        try:
            data = b64decode(msg.value.get('data'))
            dict_data = json.loads(data)
            res = client.index(index=index, doc_type='json', body=json.dumps(dict_data))
        except RequestError as request_error:
            print(request_error)
            print(data)
            raise request_error


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('python kafka2elasticsearch <topic> <index>')
        exit()

    topic = sys.argv[1]
    index = sys.argv[2]
    cpu_number = cpu_count()
    parametrs = []
    for i in range(cpu_number):
        parametrs.append((topic, index, i + 1))

    pool = Pool(processes=cpu_number)
    pool.starmap(kafka2elasticsearch, parametrs)
    pool.join()

    # kafka2elasticsearch(topic, index, 1)

import asyncio
from elasticsearch_async import AsyncElasticsearch
from kafkaconsumer_svc import create_kafka_consumer
from config import ELASTICSEARCH


def create_client_aioelasticsearch(hosts=ELASTICSEARCH):
    return AsyncElasticsearch(
        [hosts],
        scheme="http",
        port=80,
    )


client = create_client_aioelasticsearch()
consumer = create_kafka_consumer(topic=topic, group_id=index, bootstrap_servers=BROKERS)

async def print_info():
    info = await client.info()
    print(info)


def aiorun(func):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func())
    loop.run_until_complete(client.transport.close())
    loop.close()

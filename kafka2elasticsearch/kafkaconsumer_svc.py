from kafka import KafkaConsumer
import json
from config import MAX_PARTITION_FETCH_BYTES, AUTO_OFFSET_RESET


def create_kafka_consumer(topic,
                          group_id,
                          bootstrap_servers,
                          max_partition_fetch_bytes=MAX_PARTITION_FETCH_BYTES,
                          auto_offset_reset=AUTO_OFFSET_RESET,
                          enable_auto_commit=False,
                          ):
    return KafkaConsumer(topic,
                         group_id=group_id,
                         bootstrap_servers=bootstrap_servers,
                         max_partition_fetch_bytes=max_partition_fetch_bytes,
                         auto_offset_reset=auto_offset_reset,
                         enable_auto_commit=enable_auto_commit,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                         )

#!/usr/bin/env python

import logging
import os
import time
import sys

from kafka import KafkaConsumer
from prometheus_client import start_http_server, Summary, Counter

latency = Summary('request_latency_seconds', 'Latency', ['topic'])
errors = Counter('request_errors', 'Errors', ['topic'])

logging.basicConfig(level=logging.INFO)
	
def listen(consumer_instance):
    while True:
        try:
            for event in consumer_instance:
                logging.info(event)
                value = event.value.decode("utf-8")
                try:
                    latency.labels(event.topic).observe(int(value))
                except:
                    errors.labels(event.topic).inc()
                logging.info(f"Message Received: ({value})")
           # consumer_instance.close()
            logging.info("Waiting 1s for next poll")
            time.sleep(1)
        except Exception as ex:
            logging.info('Exception in subscribing')
            logging.info(str(ex))

def get_kafka_consumer(topic_name, servers=['kafka:9092']):
    _consumer = None
    logging.info(f"Starting consuming topic {topic_name}")
    try:
        _consumer = KafkaConsumer(topic_name,  bootstrap_servers=servers, consumer_timeout_ms=10000, group_id="app")
        _consumer.subscribe(['test_topic_a', 'test_topic_b'])
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer

if __name__ == "__main__":
    start_http_server(8000)
    topic = sys.argv[1]
    consumer = get_kafka_consumer(topic)
    listen(consumer)

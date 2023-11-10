import json
import time
from enum import Enum

from aiokafka import AIOKafkaProducer
from confluent_kafka import Producer

from .eventregistration import kafka_topic_events
from .exceptions import InvalidEventTopicException, InvalidEventModelForTopic, DelayQueueTopicNotSetException, \
    InvalidProduceEventParameters, InvalidDelayEventParameters
from .topics.topics import KafkaTopic
from .events.base import KafkaEvent
from velilogger import get_tracing_id


class ValueEnum(Enum):
    def __getattr__(cls, name):
        try:
            return cls[name].value
        except KeyError:
            raise AttributeError(f"'{cls.__name__}' object has no attribute '{name}'")


class DelayEventParam(ValueEnum):
    # How many times has event been dropped to a delay queue
    DELAY_COUNT = 'delay_count'

    # When was the event last dropped to the delay queue
    INIT_TIME = 'init_time'

    # To which topic should the event be sent after delay
    SOURCE_TOPIC = 'source_topic'

    # From which topic was this event consumed originally
    ORIGINAL_TOPIC = 'original_topic'


class AsyncKafkaEventProducer:

    def __init__(self, bootstrap_servers):
        self.kafka_topic_events = kafka_topic_events
        self.producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_servers
        )

    async def start(self):
        await self.producer.start()

    async def stop(self):
        await self.producer.flush()
        await self.producer.stop()

    async def produce_event(self, topic: KafkaTopic, event: KafkaEvent):
        if topic not in self.kafka_topic_events.topic_event_models:
            raise InvalidEventTopicException(f"Topic {topic} not found")
        topic_event_model = self.kafka_topic_events.topic_event_models[topic]
        if not isinstance(event, topic_event_model):
            raise InvalidEventModelForTopic(f"event: {str(event)} topic model: {str(topic_event_model)}")
        event.tracing_id = get_tracing_id()
        await self.producer.send(topic, json.dumps(event.dict()).encode())

    async def produce_easy_event(self, topic_name, event_data):
        await self.producer.send(topic_name, json.dumps(event_data).encode())


class KafkaEventProducer:
    """
        Constructor Parameters:
            bootstrap_servers (str): kafka server urls, separated by ";"
            delay_queue_topic: (str): topic name for a "delay queue"
            app_dedicated_topic: (str): topic name for events which come out of the "delay queue" (a dedicated topic
            for the app to process event after it's been in a "delay queue"
    """

    def __init__(self, bootstrap_servers, delay_queue_topic: str = None, app_dedicated_topic: str = None):
        self.delay_queue_topic = delay_queue_topic
        self.app_dedicated_topic = app_dedicated_topic
        self.producer = Producer({
            'bootstrap.servers': bootstrap_servers,
            'acks': 'all'
        })

    def produce_event(self, topic_name: str, event_data: dict):
        if not topic_name or not event_data:
            raise InvalidProduceEventParameters(f"topic_name: {topic_name}, event_data: {event_data} ")
        json_data = json.dumps(event_data).encode()
        self.producer.produce(topic_name, json_data)

    def delay_event(self, original_topic: str, event_data: dict):
        if not self.delay_queue_topic:
            raise DelayQueueTopicNotSetException()

        if not original_topic or not event_data:
            raise InvalidDelayEventParameters(f"original_topic: {original_topic}, event_data: {event_data}")

        # Set variables for "delay queue"
        event_data[DelayEventParam.DELAY_COUNT] = event_data.get(DelayEventParam.DELAY_COUNT, 0) + 1
        event_data[DelayEventParam.INIT_TIME] = time.time()
        event_data[DelayEventParam.SOURCE_TOPIC] = self.app_dedicated_topic
        event_data[DelayEventParam.ORIGINAL_TOPIC] = event_data.get(DelayEventParam.ORIGINAL_TOPIC, original_topic)

        self.produce_event(self.delay_queue_topic, event_data)

    def flush(self, timeout=3):
        messages_left = -1
        while messages_left != 0:
            messages_left = self.producer.flush(timeout)
        return self.producer.flush(timeout)

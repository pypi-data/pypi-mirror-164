import json
import pika
from stix2 import Bundle, parse
from typing import Callable


class ChannelProvider():
    def __init__(self, hostname:str="queue", port: int=5672, username: str="root", password: str="root"):
        credentials = pika.PlainCredentials(username, password)

        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(hostname, port, "/", credentials)
        )
        self._stix_channel = None
        self._enrichment_channel = None
    

    def get_enrichment_channel(self):
        if self._enrichment_channel is None:
            new_channel = self._connection.channel()

            new_channel.exchange_declare(
                exchange="enrichment", exchange_type="fanout"
            )

            new_channel.queue_declare(queue="enrichment-queue")

            new_channel.queue_bind(
                exchange="enrichment", queue="enrichment_queue"
            )

            self._enrichment_channel = new_channel

        return self._enrichment_channel

    def get_stix_channel(self):
        new_channel = self._connection.channel()

        new_channel.queue_declare(queue="stix-queue")

        return new_channel



class Helper:
    def __init__(self, hostname:str="queue", port: int=5672, username: str="root", password: str="root") -> None:
        self.channel_provider = ChannelProvider(hostname, port, username, password)
        
        
    def listen(self, callback: Callable) -> None:
        def consume_message(ch, method, properties, body):
            bundle = parse(str(body))
            return callback(bundle)

        channel = self.channel_provider.get_enrichment_channel()
        channel.basic_consume(
            queue="enrichment-queue",
            on_message_callback=consume_message,
            auto_ack=True,
        )
        channel.start_consuming()

    def send_stix_bundle(self, bundle: Bundle) -> None:
        channel = self.channel_provider.get_stix_channel()
        channel.basic_publish(
            exchange="", routing_key="stix-queue", body=bundle.serialize()
        )
        channel.close()

    def consume_stix(self, callback: Callable) -> None:
        def consume_message(ch, method, properties, body):
            json_bundle = json.loads(body)
            bundle = parse(json_bundle)
            return callback(bundle)

        channel = self.channel_provider.get_stix_channel()
        channel.basic_consume(
            queue="stix-queue",
            on_message_callback=consume_message,
            auto_ack=True,
        )
        channel.start_consuming()

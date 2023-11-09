import pika
from python_logging_rabbitmq import RabbitMQHandler as _RabbitMQHandler


# noinspection PyTypeChecker
class RabbitHandler:
    def __init__(self, dhost: str, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.dhost = dhost
        self.connection = None
        self.channel = None

    def connect(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        conn_params = pika.ConnectionParameters(self.host, self.port, credentials=credentials)
        self.connection = pika.BlockingConnection(conn_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.dhost, durable=False, arguments={'x-max-length': 10000})
        self.channel.exchange_declare(exchange='log', exchange_type='direct', durable=False)
        self.channel.queue_bind(exchange='log', queue=self.dhost, routing_key=self.dhost)

    def get_handler(self):
        return _RabbitMQHandler(host=self.host,
                                port=self.port,
                                username=self.username,
                                password=self.password,
                                routing_key_formatter=lambda r: self.dhost,
                                declare_exchange=False,
                                level=0)

    def close(self):
        self.channel.close()
        self.connection.close()

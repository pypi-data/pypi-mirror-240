import sys
import traceback
from typing import Optional

from loguru import logger as log
from loguru._simple_sinks import StreamSink

from . import LOG
from .handlers import RabbitHandler


def handle_exception(exc_type, exc_value, exc_traceback) -> None:
    """
    Перехватывает исключения, которые находяться вне блока try-except
    и выводит traceback во все хэндлеры подключенных в логгере.

    Использование (client_code):
        sys.excepthook = handle_exception
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Форматируем исключение
    traceback_string = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(traceback_string, file=sys.stderr)

    # Логирование исключения с полным traceback
    log.error(traceback_string)


class LogTool:
    def __init__(self):
        self._rabbit: Optional[RabbitHandler] = None
        self.__set_default_logging()

    @staticmethod
    def __set_default_logging() -> None:
        log.remove()
        log.add(sys.stdout, colorize=True, format=LOG.FORMAT_STDOUT, level='TRACE')
        for level, color in LOG.LEVEL_COLORS.items():
            log.level(level, color=color)

    def add_rabbitmq_logging(self, queue_name: str, username: str, password: str, host: str, port: str) -> None:
        """
        Подключить передачу логов на сервер RabbitMQ.
        :param queue_name: имя очереди, где будут храниться логи
        :param username: пользователь rabbitmq
        :param password: пароль от rabbitmq
        :param host: IP сервера где расположен rabbitmq
        :param port: Порт сервера
        :return: None
        """
        self._rabbit = RabbitHandler(queue_name, username, password, host, port)
        handler = self._rabbit.get_handler()
        log.add(handler, colorize=False, level=LOG.TRACE, format=LOG.FORMAT_STDOUT)

    @staticmethod
    def add_file_logging(filepath: str) -> None:
        """
        Подключить handler на запись логов в файл.
        :param filepath: абсолютный путь файла
        :return: None
        """
        log.add(filepath, colorize=False, level=LOG.TRACE, format=LOG.FORMAT_STDOUT, rotation=LOG.FILE_LIMIT)

    @staticmethod
    def change_level(level: str) -> None:
        """
        Изменение уровня логирования.
        :param level: TRACE | DEBUG | INFO | WARINING | ERROR
        :return: None
        """
        level = level.upper()
        handlers_config = []
        for _, handler_data in log._core.handlers.items():
            sink = handler_data._sink
            colorize = False
            if isinstance(handler_data._sink, StreamSink): colorize = True
            handlers_config.append({"sink": sink, "level": level, "colorize": colorize, "format": LOG.FORMAT_STDOUT})
        log.configure(handlers=handlers_config)

    def close(self) -> None:
        """
        Закрытие коннекта, если подключен RabbitHandler.
        :return: None
        """
        if self._rabbit:
            self._rabbit.close()


logtool = LogTool()

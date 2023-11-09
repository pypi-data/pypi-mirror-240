from dataclasses import dataclass


@dataclass
class LOG:
    TRACE = 'TRACE'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    FORMAT_STDOUT = ("<green>{time:HH:mm:ss}</green> | "
                     "<level>{level:>7}</level> | "
                     "<level>{message}</level>  "
                     "<fg #8E8E8E>{module}.{function}:{line}</fg #8E8E8E>"
                     )

    LEVEL_COLORS = {
        "TRACE": "<fg #B1B1B1>",
        "DEBUG": "<c>",
        "INFO": "<green>",
        "SUCCESS": "<bold><green>",
        "WARNING": "<yellow>",
        "ERROR": "<red><bold>",
        "CRITICAL": "<red><bold>",
    }
    FILE_LIMIT = "20 MB"

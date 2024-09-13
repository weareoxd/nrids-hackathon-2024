import json

import structlog

ALLOWED_LOG_LEVELS = {
    "alert",
    "crit",
    "debug",
    "emerg",
    "err",
    "info",
    "notice",
    "trace",
    "unknown",
    "warning",
}
timestamper = structlog.processors.TimeStamper(fmt="iso", key="@timestamp", utc=False)


def configure_structlog():
    """
    Setup structlog configuration.

    Individual loggers are in Django settings.
    """
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            timestamper,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        context_class=structlog.threadlocal.wrap_dict(dict),
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def format_levels_for_elasticsearch(event_dict):
    """
    Normalize levels as expected by Elasticsearch:
    https://github.com/ViaQ/elasticsearch-templates/blob/master/\
        namespaces/_default_.yml#L76
    """
    level = event_dict.get("level", "").lower()
    if level == "critical":
        event_dict["level"] = "crit"
    elif level == "error":
        event_dict["level"] = "err"
    elif level in ALLOWED_LOG_LEVELS:
        event_dict["level"] = level
    else:
        event_dict["level"] = "unknown"

    return event_dict


def set_message_for_elasticsearch(event_dict):
    """
    The 'message' key is required.
    """
    event_dict["message"] = event_dict.pop("event", "")

    return event_dict


def fluentd_json(event_dict, **kwargs):
    """
    Fluentd compatible JSON format.
    """
    event_dict = set_message_for_elasticsearch(event_dict)
    event_dict = format_levels_for_elasticsearch(event_dict)

    # Convert all values to string; nulls or numbers cause errors
    # When indexed in Elasticsearch
    for key, value in event_dict.items():
        if not isinstance(value, str):
            event_dict[key] = str(value)

    return json.dumps(event_dict, **kwargs)

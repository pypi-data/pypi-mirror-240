import logging

import aglog

aglog.dict_config_from_yaml("./notebook/logging_conf.yaml")

try:
    1 / 0  # noqa: B018 # type: ignore
finally:
    logging.exception("This is a info message", extra={"user": "aglog"})

logging.info("This is a info message", extra={"user": "aglog"}, stack_info=True)

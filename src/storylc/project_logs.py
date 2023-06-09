import logging
import logging.config
from pathlib import Path

import yaml


def init_logs() -> None:
    """
    this loads the yaml file for configuring the logs

    keep in mind that the handlers in dev will be different from the
    handlers in prod.

    :return:
    """
    logfile = Path(__file__).parent / "logging.yml"
    if not logfile.exists():
        raise FileNotFoundError(logfile)
    data = yaml.load(logfile.read_text(), yaml.FullLoader)
    logging.config.dictConfig(data)


# not necessary, but it's convenient to have variables to name your loggers
# I know that it is usual to write :
# logger = logging.getLogger(__name__), but I (personal taste) find it more powerful to have name topics,
# such as ETL, model optimization, gers int, ... whatever you like.
# remember that topic is not handler. You can have different topics routed to a same handler.
a_logger = logging.getLogger("A-topic")

b_logger: logging.Logger = logging.getLogger("B-topic")
error_logger: logging.Logger = logging.getLogger("error-topic")
exception_logger: logging.Logger = logging.getLogger("exception-topic")

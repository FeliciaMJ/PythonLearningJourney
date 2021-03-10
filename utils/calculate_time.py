import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s -> %(levelname)s -> |%(message)s|')
logger = logging.getLogger(__name__)


def calculate_time(fn):
    """ test the function running time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = fn(*args, **kwargs)
        end_time = time.time()
        logger.info("%s() running costs time is : %s ms" % (fn.__name__, 1000*(end_time - start_time)))
        return f
    return wrapper

import time
from utils.my_logger import logger


def calculate_time(fn):
    """ test the function running time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = fn(*args, **kwargs)
        end_time = time.time()
        logger().info("%s() running costs time is : %s ms" % (fn.__name__, 1000*(end_time - start_time)))
        return f
    return wrapper

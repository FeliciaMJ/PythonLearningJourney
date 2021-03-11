import logging


def logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s -> %(levelname)s -> %(message)s")
    my_logger = logging.getLogger(__name__)
    return my_logger


if __name__ == '__main__':
    # logger = logger()
    logger().info("hello world!")

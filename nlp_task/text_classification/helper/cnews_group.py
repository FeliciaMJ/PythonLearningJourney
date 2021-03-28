import os
from utils.my_logger import logger


def get_data_dir() -> str:
    """
    获取cnews的文件路径，其中包含本任务需要的数据。
    :return:
    """
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
    data_dir = os.path.join(root_dir, "data_source", "cnews")
    return data_dir


def _read_file(filename: str) -> str:
    """
    读取文件的内容，并将文件中的制表符、换行符以及中文换行符替换为空字符。
    :param filename:
    :return:
    """
    with open(filename, mode="r", encoding="UTF-8") as reader:
        """
        1.不间断空格\u00A0,主要用在office中,让一个单词在结尾处不会换行显示,快捷键ctrl+shift+space ;
        2.半角空格(英文符号)\u0020,代码中常用的;
        3.全角空格(中文符号)\u3000,中文文章中使用;
        """
        return reader.read().replace("\n", "").replace("\t", "").replace("\u3000", "")


def print_data_number(data_apply: str):
    """
    打印每种数据集对应的样本数量。
    :param data_apply:
    :return:
    """
    data_file = os.path.join(get_data_dir(), data_apply)
    with open(data_file, mode="r", encoding="UTF-8") as reader:
        logger().info(data_file.split("/")[-1] + " has " + str(len(reader.readlines())) + " examples !")


if __name__ == '__main__':
    parameter = ["cnews.train.txt", "cnews.test.txt", "cnews.val.txt"]
    for data_name in parameter:
        print_data_number(data_name)

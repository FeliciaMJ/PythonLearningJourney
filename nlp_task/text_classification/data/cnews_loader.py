import sys
from collections import Counter

import numpy as np
import tensorflow.python.keras as kr

from utils.my_logger import logger

if sys.version_info[0] == 3:
    is_py3 = True
else:
    is_py3 = False


def native_word(word: str, encoding="UTF-8"):
    """

    :param word:
    :param encoding:
    :return:
    """
    if not is_py3:
        return word.encode(encoding)
    else:
        return word


def native_content(content: str):
    """

    :param content:
    :return:
    """
    if not is_py3:
        return content.decode("UTF-8")
    else:
        return content


def open_file(filename: str, mode="r"):
    """

    :param filename:
    :param mode:
    :return:
    """
    if is_py3:
        return open(filename, mode, encoding="UTF-8", errors="ignore")
    else:
        return open(filename, mode)


def read_file(filename: str) -> tuple:
    """

    :param filename:
    :return:
    """
    contents, labels = [], []
    with open_file(filename) as reader:
        for line in reader:
            try:
                label, content = line.strip().strip("\t")
                if content:
                    contents.append(list(native_content(content)))
                    labels.append(native_content(label))
            except:
                logger().info("跳过...")
    return contents, labels


def build_vocab(train_dir: str, vocab_dir: str, vocab_size=5000):
    """

    :param train_dir:
    :param vocab_dir:
    :param vocab_size:
    :return:
    """
    data_train, _ = read_file(train_dir)
    all_data = []
    for content in data_train:
        all_data.extend(content)

    counter = Counter(all_data)
    counter_pairs = counter.most_common(vocab_size - 1)
    words, _ = list(zip(*counter_pairs))
    words = ["<PAD>"] + list(words)
    open_file(vocab_dir, mode="w").write("\n".join(words) + "\n")


def read_vocab(vocab_dir: str) -> tuple:
    """

    :param vocab_dir:
    :return:
    """
    with open_file(vocab_dir) as reader:
        words = [native_content(_.strip()) for _ in reader.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id


def read_category() -> tuple:
    """

    :return:
    """
    categories = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
    categories = [native_content(x) for x in categories]
    cat_to_id = dict(zip(categories, range(len(categories))))
    return categories, cat_to_id


def to_words(content: str, words: dict) -> str:
    """

    :param content:
    :param words:
    :return:
    """
    return "".join(words[x] for x in content)


def process_file(filename: str, word_to_id: dict, cat_to_id: dict, max_length=600) -> tuple:
    """

    :param filename:
    :param word_to_id:
    :param cat_to_id:
    :param max_length:
    :return:
    """
    contents, labels = read_file(filename)
    data_id, label_id = [], []
    for i in range(len(contents)):
        data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
        label_id.append(cat_to_id[labels[i]])

    x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
    y_pad = kr.utils.to_categorical(label_id, num_classes=len(cat_to_id))

    return x_pad, y_pad


def batch_iter(x: np.array, y: np.array, batch_size=64):
    """

    :param x:
    :param y:
    :param batch_size:
    :return:
    """
    data_len = len(x)
    num_batch = int((data_len - 1) / batch_size) + 1
    indices = np.random.permutation(np.arange(data_len))
    x_shuffle = x[indices]
    y_shuffle = y[indices]

    for i in range(num_batch):
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]

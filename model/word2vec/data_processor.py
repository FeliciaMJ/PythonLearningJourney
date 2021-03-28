import os
import zipfile
import tensorflow as tf
import numpy as np
import collections
import random
import math
import argparse


parser = argparse.ArgumentParser(description='Word2Vector参数设置')

parser.add_argument('--batch_size', type=int, default=128, help='')
parser.add_argument('--embedding_size', type=int, default=128, help='')
parser.add_argument('--skip_window', type=int, default=1, help='')
parser.add_argument('--num_skips', type=int, default=2, help='')
parser.add_argument('--valid_size', type=int, default=16, help='')
parser.add_argument('--valid_window', type=int, default=100, help='')
parser.add_argument('--num_sampled', type=int, default=64, help='')
parser.add_argument('--num_steps', type=int, default=100001, help='')
parser.add_argument('--cbow_window', type=int, default=1, help='')
parser.add_argument('--vocabulary_size', type=int, default=50000, help='')

args = parser.parse_args()

data_index = 0


def data_dir(file_name: str) -> str:
    """
    获取语料所在的路径。统一将所有的语料都放在data source路径下。
    :param file_name:
    :return:
    """
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
    data_path = os.path.join(parent_dir, "data_source", file_name)
    return data_path


def read_data(filename: str) -> list:
    """
    将语料库中的语料读成列表形式。
    :param filename: 语料库所在的路径。
    :return:
    """
    with zipfile.ZipFile(filename) as f:
        corpus = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return corpus


def build_dataset(words: list, n_words: int) -> tuple:
    """
    构建语料字典。
    :param words: 语料的列表表示。
    :param n_words: 提取所有语料中的前n个词。
    :return:
    """
    dictionary_inner = {}
    count_inner = [["UNK", 0]]
    count_inner.extend(collections.Counter(words).most_common(n_words-1))
    # 出现次数越高的词，对应的index越小。
    for word, _ in count_inner:
        dictionary_inner[word] = len(dictionary_inner)
    data_inner = []
    unk_count = 0
    for word in words:
        if word in dictionary_inner:
            index = dictionary_inner[word]
        else:
            index = 0
            unk_count += 1
        data_inner.append(index)
    count_inner[0][1] = unk_count
    reverse_dictionary_inner = {key: value for value, key in dictionary_inner.items()}
    return data_inner, count_inner, dictionary_inner, reverse_dictionary_inner


def generate_batch_for_cbow(batch_size: int, cbow_window: int, data: list):
    """
    为CBOW模型生成训练数据，喂入模型。
    :param data:
    :param batch_size: 每个batch里面的数据个数
    :param cbow_window: 每个词要考虑的上下文单词个数。
    :return:
    """
    global data_index
    assert cbow_window % 2 == 1
    span = 2 * cbow_window + 1
    batch = np.ndarray(shape=(batch_size, span-1), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)

    buffer = collections.deque(maxlen=span)
    for _ in range(span):
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)

    for i in range(batch_size):
        target = cbow_window
        col_idx = 0
        for j in range(span):
            # 略过中心元素 word
            if j == span // 2:
                continue
            batch[i, col_idx] = buffer[j]
            col_idx += 1
        labels[i, 0] = buffer[target]
        # 更新 buffer
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)

    return batch, labels


def generate_data_for_skip_gram(batch_size, num_skips, skip_window):
    """
    为skip_gram模型生成训练数据，喂入模型。
    :param batch_size:
    :param num_skips:
    :param skip_window:
    :return:
    """
    global data_index
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1
    buffer = collections.deque(maxlen=span)
    for _ in range(span):
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)

    for i in range(batch_size // num_skips):
        target = skip_window
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[skip_window]
            labels[i * num_skips + j, 0] = buffer[target]
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    data_index = (data_index + len(data) - span) % len(data)
    return batch, labels


class CBOWModel(object):
    def __init__(self, filename):
        self.corpus = read_data(data_dir(filename))
        self.data, self.count, self.dictionary, self.reverse_dictionary = build_dataset(self.corpus,
                                                                                        self.vocabulary_size)
        self.valid_window = args.valid_window
        self.valid_size = args.valid_size
        self.batch_size = args.batch_size
        self.cbow_window = args.cbow_window
        self.vocabulary_size = args.vocabulary_size
        self.embedding_size = args.embedding_size
        self.graph = tf.Graph()

    def generate_valid_examples(self):
        valid_examples = np.array(random.sample(range(self.valid_window), self.valid_size // 2))
        valid_examples = np.append(
            valid_examples, random.sample(range(1000, 1000 + self.valid_window), self.valid_size // 2))
        return valid_examples

    def generate_input_data(self):
        self.train_dataset = tf.placeholder(tf.int32, shape=[self.batch_size, 2 * self.cbow_window + 1])
        self.train_labels = tf.placeholder(tf.int32, shape=[self.batch_size, 1])
        self.valid_dataset = tf.constant(self.generate_valid_examples())
        self.embeddings = tf.Variable(tf.random_uniform([self.vocabulary_size, self.embedding_size], -1.0, 1.0))
        self.nce_weights = tf.Variable(
            tf.truncated_normal([self.vocabulary_size, self.embedding_size], stddev=1.0 / math.sqrt(embedding_size))
        )
        self.nce_biases = tf.Variable(tf.zeros([self.vocabulary_size]))




if __name__ == '__main__':
    vocabulary_size = 50000
    data_first = read_data(data_dir("text8.zip"))
    # data: [1, 2, 3, 555, 6664, 12365, ...]
    # count: [(item: item frequency), ...]
    # dictionary: {item: index,...}
    # reverse_dictionary: {index: item, ...}
    data, count, dictionary, reverse_dictionary = build_dataset(data_first, vocabulary_size)
    # 训练的步数
    num_steps = 1000001
    # 每步训练中的词个数
    batch_size = 128
    # 嵌入词的维度
    embedding_size = 128
    # 每个词要考虑的上下文词的个数，如果是1，则上文考虑一个，下文考虑一个。
    cbow_window = 1

    # We pick a random validation set to sample nearest neighbors. here we limit the
    # validation samples to the words that have a low numeric ID, which by
    # construction are also the most frequent.
    valid_size = 16  # Random set of words to evaluate similarity on.
    valid_window = 100  # Only pick dev samples in the head of the distribution.
    # pick 16 samples from 100
    valid_examples = np.array(random.sample(range(valid_window), valid_size // 2))
    valid_examples = np.append(valid_examples, random.sample(range(1000, 1000 + valid_window), valid_size // 2))
    num_sampled = 64  # Number of negative examples to sample.

    graph = tf.Graph()

    with graph.as_default(), tf.device('/cpu:0'):

        # Input data.
        train_dataset = tf.placeholder(tf.int32, shape=[batch_size, 2 * cbow_window])
        train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
        valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

        # Variables.
        # embedding, vector for each word in the vocabulary
        embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

        nce_weights = tf.Variable(
            tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))

        nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

        # Model.
        # Look up embeddings for inputs.
        # this might efficiently find the embeddings for given ids (trained dataset)
        # manually doing this might not be efficient given there are 50000 entries in embeddings
        embeds = None
        for i in range(2 * cbow_window):
            embedding_i = tf.nn.embedding_lookup(embeddings, train_dataset[:, i])
            print('embedding %d shape: %s' % (i, embedding_i.get_shape().as_list()))
            emb_x, emb_y = embedding_i.get_shape().as_list()
            if embeds is None:
                embeds = tf.reshape(embedding_i, [emb_x, emb_y, 1])
            else:
                embeds = tf.concat([embeds, tf.reshape(embedding_i, [emb_x, emb_y, 1])], 2)

        assert embeds.get_shape().as_list()[2] == 2 * cbow_window
        print("Concat embedding size: %s" % embeds.get_shape().as_list())
        avg_embed = tf.reduce_mean(embeds, 2, keep_dims=False)
        print("Avg embedding size: %s" % avg_embed.get_shape().as_list())

        loss = tf.reduce_mean(tf.nn.nce_loss(nce_weights, nce_biases,
                                             labels=train_labels,
                                             inputs=avg_embed,
                                             num_sampled=num_sampled,
                                             num_classes=vocabulary_size))

        # Optimizer.
        # Note: The optimizer will optimize the softmax_weights AND the embeddings.
        # This is because the embeddings are defined as a variable quantity and the
        # optimizer's `minimize` method will by default modify all variable quantities
        # that contribute to the tensor it is passed.
        # See docs on `tf.train.Optimizer.minimize()` for more details.
        # Adagrad is required because there are too many things to optimize
        optimizer = tf.train.AdagradOptimizer(1.0).minimize(loss)

        # Compute the similarity between minibatch examples and all embeddings.
        # We use the cosine distance:
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
        normalized_embeddings = embeddings / norm
        valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, valid_dataset)
        similarity = tf.matmul(valid_embeddings, tf.transpose(normalized_embeddings))

    with tf.Session(graph=graph) as session:
        tf.global_variables_initializer().run()
        average_loss = 0
        for step in range(num_steps):
            batch_data, batch_labels = generate_batch_for_cbow(batch_size, cbow_window, data)
            feed_dict = {train_dataset: batch_data, train_labels: batch_labels}
            _, loss_calculate = session.run([optimizer, loss], feed_dict=feed_dict)
            average_loss += loss_calculate
            if step % 2000 == 0:
                if step > 0:
                    average_loss = average_loss / 2000
                    # The average loss is an estimate of the loss over the last 2000 batches.
                print('Average loss at step %d: %f' % (step, average_loss))
                average_loss = 0
            # note that this is expensive (~20% slowdown if computed every 500 steps)
            if step % 10000 == 0:
                sim = similarity.eval()
                for i in range(valid_size):
                    valid_word = reverse_dictionary[valid_examples[i]]
                    top_k = 8  # number of nearest neighbors
                    nearest = (-sim[i, :]).argsort()[1:top_k + 1]
                    log = 'Nearest to %s:' % valid_word
                    for k in range(top_k):
                        close_word = reverse_dictionary[nearest[k]]
                        log = '%s %s,' % (log, close_word)
                    print(log)
        final_embeddings = normalized_embeddings.eval()


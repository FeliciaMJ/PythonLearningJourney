import tensorflow as tf


class TCNNConfig(object):
    embedding_dim = 64  # 词向量的维度
    seq_length = 600  # 序列长度
    num_class = 10  # 类别数
    num_filters = 256  # 卷积核数
    kernel_size = 5  # 卷积核尺寸
    vocab_size = 5000  # 词汇表大小

    hidden_dim = 128  # 全连接层神经元数
    dropout_keep_prob = 0.5  # dropout保留比例
    learning_rate = 1e-3  # 学习率
    batch_size = 64  # 每批训练大小
    num_epochs = 10  # 总迭代次数
    print_per_batch = 100  # 每多少轮输出一次结果
    save_per_batch = 30  # 每多少轮存入tensorboard


class TextCNN(object):
    def __init__(self, config):
        self.config = config

        self.input_x = tf.placeholder(dtype=tf.int32, shape=[None, self.config.seq_length], name="input_x")
        self.input_y = tf.placeholder(dtype=tf.float32, shape=[None, self.config.num_class], name="input_y")
        self.keep_prob = tf.placeholder(dtype=tf.float32, name="keep_prob")
        self.cnn()

    def cnn(self):
        with tf.device("/cpu:0"):
            embedding = tf.get_variable(name="embedding", shape=[self.config.vocab_size, self.config.embedding_dim])
            embedding_inputs = tf.nn.embedding_lookup(embedding, self.input_x)

        with tf.name_scope("cnn"):
            conv = tf.layers.conv1d(embedding_inputs, self.config.num_filters, self.config.kernel_size, name="conv")
            gmp = tf.reduce_max(conv, reduction_indices=[1], name="gmp")

        with tf.name_scope("score"):
            fc = tf.layers.dense(gmp, self.config.hidden_dim, name="fc")
            fc = tf.contrib.layers.dropout(fc, self.keep_prob)
            fc = tf.nn.relu(fc)

            self.logits = tf.layers.dense(fc, self.config.num_class, name="fc2")
            self.y_pred_cls = tf.arg_max(tf.nn.softmax(self.logits), 1)

        with tf.name_scope("optimize"):
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits, labels=self.input_y)
            self.loss = tf.reduce_mean(cross_entropy)
            self.optim = tf.train.AdamOptimizer(learning_rate=self.config.learning_rate).minimize(self.loss)

        with tf.name_scope("accuracy"):
            correct_pred = tf.equal(tf.arg_max(self.input_y, 1), self.y_pred_cls)
            self.acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))


if __name__ == '__main__':
    tcc = TCNNConfig()
    print(tcc.__dict__)
import tensorflow as tf


var1 = tf.Variable(5, name="var1")
var2 = tf.Variable(6)

var3 = tf.Variable(initial_value=tf.random_uniform(shape=(2, 3), minval=10, maxval=20), name="var3")
var4 = tf.Variable(tf.truncated_normal(shape=[2, 3], mean=2.0, stddev=0.5, dtype=tf.float32, seed=234), name="var4")
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(var1))
    print(sess.run(var1 + var2))
    print(sess.run(var3))
    # print(sess.run(var4))



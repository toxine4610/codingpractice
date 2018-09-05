import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


'''
default np.pi only has 18 digits, but for this task, we need to generate 10,000 digits of pi.
one potential solution is to use the symbolic math toolbox.
another potential solution is to generate the 10,000 digits of pi using some algorithm
'''

def weightCorrects(correct):

    from mpmath import mp
    mp.dps = len(correct)+1
    
    xs = str(np.sqrt(mp.pi))
    # remove the decimal place
    pi_digits = [ x for x in xs if x != '.' ]
    
    num = 0 
    den = 0

    for i in range( len(correct) ):
        correct_this_index = correct[i] * int(pi_digits[i])
        num += (correct_this_index)
        den += int( pi_digits[i] )
    return float(num/den)


with tf.Session() as sess:
    
    
    saver = tf.train.import_meta_graph('model.ckpt.meta')
    saver.restore(sess, 'model.ckpt')

    variables = tf.global_variables()
    Ws = [var for var in variables if len(var.get_shape()) == 2]
    Bs = [var for var in variables if len(var.get_shape()) == 1]
    assert(len(Ws) == len(Bs))
    x_tf = sess.graph.get_tensor_by_name('x:0')
    y_tf = sess.graph.get_tensor_by_name('y:0')

    nonlinearities = [tf.identity for i in range(len(Ws) - 1)] + [tf.nn.softmax]
    out = x_tf
    for W, b, nonlinearity in zip(Ws, Bs, nonlinearities):
        out = nonlinearity(tf.nn.xw_plus_b(out, weights=W, biases=b))

    correct_tf = tf.cast(tf.equal(tf.cast(tf.argmax(out, -1), tf.int32), y_tf), tf.int32)

    test = input_data.read_data_sets("/tmp", False).test
    correct = sess.run(correct_tf, feed_dict={x_tf: test.images,
                                              y_tf: test.labels})

    print("Pi-weighted Accuracy: {:.60f}".format(weightCorrects(correct)))
    print("Accuracy: {:.10f}".format(np.mean(correct)))

# -*- coding: utf-8 -*-
## multi-layer perceptron for MNIST classifcation

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# params
learning_rate = 0.001
training_epochs = 30
lambda_term = 0.01
batch_size = 100
display_step = 5
total_batch = (mnist.train.num_examples//batch_size)


#network params
n_hidden_1 = 256
n_hidden_2 = 256
n_hidden_3 = 256
n_input    = 28*28
n_classes  = 10

# determine std dev of intialized weight matrix using xavier-he
def  xavier_init (fan_in, fan_out, constant=1): 
    """ Xavier initialization of network weights"""
    # https://stackoverflow.com/questions/33640581/how-to-do-xavier-initialization-on-tensorflow
    low = -constant*np.sqrt(6.0/(fan_in + fan_out)) 
    high = constant*np.sqrt(6.0/(fan_in + fan_out))
    return tf.random_uniform((fan_in, fan_out), 
                             minval=low, maxval=high, 
                             dtype=tf.float32)

# define TF placeholders for data (image vectors) and labels (1x10 vector)
Data = tf.placeholder(tf.float32, [None, n_input] )
Label = tf.placeholder(tf.float32, [None, n_classes] )
keep_prob = tf.placeholder(tf.float32)

# make a dictionary of weights (matrix) and biases (Vector), and initialize them with white noise
weights = { 
        'l1' : tf.Variable(xavier_init(n_input, n_hidden_1)), # 784 --> 256
        'l2' : tf.Variable(xavier_init(n_hidden_1, n_hidden_2)), # 256 --> 256
        'l3' : tf.Variable(xavier_init(n_hidden_2, n_hidden_3)),
        'out': tf.Variable(xavier_init(n_hidden_2, n_classes)) # 256 --> 10
        }
bias = {
        'l1' : tf.Variable(tf.random_normal([n_hidden_1])),
        'l2' : tf.Variable(tf.random_normal([n_hidden_2])),
        'l3' : tf.Variable(tf.random_normal([n_hidden_3])),
        'out': tf.Variable(tf.random_normal([n_classes]))
        }

# make a 3 layer perceptron
def multiLayerPerceptron(x):
    layer1 = tf.nn.relu( tf.add(tf.matmul(x,weights['l1']),bias['l1']) )

    layer2 = tf.nn.relu( tf.add(tf.matmul(layer1,weights['l2']),bias['l2']) )
    layer2_do  = tf.nn.dropout(layer2,keep_prob)
    
    layer3 = tf.nn.relu( tf.add(tf.matmul(layer2_do, weights['l3']),bias['l3']) )
    layer3_do  = tf.nn.dropout(layer3,keep_prob)

    layer_out = tf.add(tf.matmul(layer3_do,weights['out']),bias['out'])
    return layer_out

logits  = multiLayerPerceptron(Data)

'''
use ADAM stochastic gradient descent to minimize the cost function 
cost function = joint entropy between the predicted and actual labels with regularization
'''
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,labels=Label)
                        + lambda_term*tf.nn.l2_loss(weights['l1'])
                        + lambda_term*tf.nn.l2_loss(bias['l1'])
                        + lambda_term*tf.nn.l2_loss(weights['l2'])
                        + lambda_term*tf.nn.l2_loss(bias['l2'])
                        + lambda_term*tf.nn.l2_loss(weights['l2'])
                        + lambda_term*tf.nn.l2_loss(bias['l2'])
                        + lambda_term*tf.nn.l2_loss(weights['l3'])
                        + lambda_term*tf.nn.l2_loss(bias['l3'])
                        )

train_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss_op) 

'''
initialize
'''
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    ac = []
    for epoch in range(training_epochs):
        avg_cost = 0.
        # mini batch backprop training
        for i in range(total_batch):
            batch_data, batch_label = mnist.train.next_batch(batch_size)
            _,c = sess.run([train_op,loss_op],feed_dict={Data:batch_data,Label:batch_label,keep_prob:0.5})
            avg_cost = avg_cost + c/total_batch
            ac.append(avg_cost)
        if epoch % display_step == 0:
            print("Epoch: {}, cost={:.9f}".format(epoch+1, avg_cost))
    print("Optimization Finished!")
    
    # test model
    pred = tf.nn.softmax(logits)
    corr_pred = tf.equal(tf.argmax(pred,1), tf.argmax(Label,1))
    accuracy  = tf.reduce_mean(tf.cast(corr_pred, tf.float32))
    print("Accuracy:", accuracy.eval({Data:mnist.test.images, Label:mnist.test.labels,keep_prob:1.0}))
    v = sess.run(bias['l2'])
    
# plt.figure(num=1)
# plt.plot(ac)
# plt.show()

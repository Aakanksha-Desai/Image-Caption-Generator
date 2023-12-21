# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:48:38 2020

@author: aakan
"""

import tensorflow as tf
#a = tf.compat.v1.placeholder(tf.float32)
#b = tf.compat.v1.placeholder(tf.float32)
#add = a + b
#tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.Session()
#output = sess.run(add, {a:[1,3], b:[2,4]})
#print(output)


variable = tf.Variable([0.9,0.7], dtype = tf.float32)
init = tf.global_variables_initializer()
#variable must be initialized before a graph is used for the first time. 

print(sess.run(init))
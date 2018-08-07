
# coding: utf-8

# In[1]:


# Example of tensorflow library
import tensorflow as tf
# declare two symbolic floating point scalars
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# create a simple symbolic expression using the add function
add = tf.add(a,b)
# bind values to a and b
sess = tf.Session()
binding = {a: 12.5, b: 2.5}
c = sess.run(add, feed_dict=binding)
print(c)


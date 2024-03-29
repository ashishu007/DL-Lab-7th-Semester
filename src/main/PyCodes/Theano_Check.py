
# coding: utf-8

# In[1]:


# example of theano library
import theano
from theano import tensor
# declare two symboic floating point scalars
a=tensor.dscalar()
b=tensor.dscalar()
# create a simple symbolic expression
c=a+b
# convert the expression into a callable object that takes (a,b) and computes c
f = theano.function([a,b],c)
# bind values to a and b and evaluate c
result = f(1.5, 2.5)
print(result)


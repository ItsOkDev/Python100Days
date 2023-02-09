#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add():
    a = 10
    b = 20
    c = a + b
    return c


# In[3]:


add()


# In[4]:


def sub(a,b):
    c = a + b
    return c


# In[6]:


sub(20,10)


# In[9]:


def every(x,y):
    a = x + y
    d = x/y
    s = x - y
    m = x * y
    return a,d,s,m


# In[22]:


add,div,sub,mul = every(7,5)


# In[20]:


mul


# In[21]:


add


# In[34]:


b = 11
a = 10
def add(d):
    a = 10
    c = a+d
    return c
add(2)
print(b)
print(a)
def sub():
    x = a-b
    return x
sub()


# In[45]:


b = 20
def add(d):
    global a
    a = 2
    c = a+d
    return c
add(20)


# In[46]:


print(b)


# In[47]:


print(a)


# In[ ]:





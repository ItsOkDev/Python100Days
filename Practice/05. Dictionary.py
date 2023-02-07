#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Dictionary
d = {} #Created Empty Dictionary

stu={100:'Hello', 200:'Dev', 300:'Wassaop'}
fees={400:'Oyy', 500:'Cool', 600:'Nice'}

print(stu)
print(stu[100])
print(fees[400])


# In[9]:


#Modifying the DictionRY
stu={100:'Hi1',200:'Hi2',300:'Hi3'}
print(stu)
print("Before Mod")
print(id(stu))
stu[100] = 'HIII01'
print(stu)
print(id(stu))


# In[21]:


#Sets
x = {1,1,2,3}
print(x) #Set do not take Dublicates
type(x)


# In[ ]:





# In[32]:


x.add(33) #For Single
print(x)


# In[27]:


x.update([11,11,22,33]) #For MULTIPLE
print(x)


# In[29]:


x.discard(11)
print(x)


# In[33]:


x.remove(33)
print(x)


# In[50]:


for i in x:
    print(i, end=" ")


# In[38]:


y = x.copy()
print(y)


# In[46]:


a = {1,2,3,4,5,6}
b = {1,2,3,44,55,66}
a1 = a.intersection(b)
a1


# In[48]:


a = {1,2,3,4,5,6}
b = {1,2,3,44,55,66}
a2 = a.union(b)
a2


# In[49]:


a = {1,2,3,4,5,6}
b = {1,2,3,44,55,66}
a3 = a.difference(b)
a3


# In[54]:


a = {1,2,3,4,5,6}  #All value of a meed to b in b
b = {1,2,3,4,5,6}
a4 = a.issubset(b)
a4


# In[56]:


a = {1,2,3,4,5,6}
b = {1,2,3,4,5,6,7,8}
a5 = a.issubset(b)
a5


# In[62]:


a = {1,2,3,4,5,6,7}   #Institute inside has Class b
b = {1,2,3,4,5,6}
a6 = a.issuperset(b)
a6


# In[ ]:





# In[59]:


d={4,5,6}
e={4,5,6,7}


# In[60]:


d.issubset(e)


# In[61]:


e.issuperset(d)


# In[64]:


n = int(input("Enter The range "))
x = []
for i in range(n):
    d = int(input("Enter valur"))
    x.append(d)
print(x)


# In[69]:


n = int(input("Enter The range "))
x = []
for i in range(n):
    d = int(input("Enter valur"))
    x.append(d)
x = tuple(x)
print(x)


# ## 

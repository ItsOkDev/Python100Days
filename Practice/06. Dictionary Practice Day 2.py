#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = {} #Created Empty Dictionary

stu={100:'Hello', 200:'Dev', 300:'Wassaop'}
fees={400:'Oyy', 500:'Cool', 600:'Nice'}

print(stu)
print(stu[100])
print(fees[400])


# In[13]:


l = {100:'Hello', 200:'Dev', 300:'Wassaop'}
for i in l.items():
    print(i)


# In[15]:


for i in l.keys():
    print(i)
for i in l.values():
    print(i)


# In[51]:


a = int(input("Enter Range: "))
nor = []
eve = []
odd = []
for i in range(a):
    x = int(input("Enter Values "))
    nor.append(x)
print("NORMAL is ", nor)
for i in nor:
    if i%2==0:
#print("Eve Number is ")
        eve.append(i)
    else:
#print("ODD Number is ")
        odd.append(i)
print("ODD is ", odd)
print("EVEN is", eve)


# 

# ## 

# In[50]:


n = int(input("Enter The range "))
x = []
for i in range(n):
    d = int(input("Enter valur"))
    x.append(d)
x = tuple(x)
print(x)


# In[55]:


l = {100:'Hello', 200:'Dev', 300:'Wassaop'}
l[400]="LOLL"
l


# In[58]:


l = {100:'Hello', 200:'Dev', 300:'Wassaop'}
l.update({400:'LOl'})
l


# In[61]:


l = {100:'Hello', 200:'Dev', 300:'Wassaop'}
p = {1:'x',2:'y',3:'z'}
l.update(p)
print(l)


# In[88]:


# User Defined Dictionary
d = {}
p = int(input("range"))
for i in range(p):
    a = input("Enter key ")
    b  = input("Enter VAl ")
    d.update({a:b})
print(d)


# 

# In[ ]:





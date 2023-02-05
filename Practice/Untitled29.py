#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Remove the Same Numbers and print 
l = [1,2,3,4,10,10,10,3,3,2,1,1]
a1 = []
for i in l:
    if i not in a1:
        a1.append(i)
print(a1)


# In[2]:


set(l)


# In[ ]:





# In[13]:


# Calculating the Uppers/ And Lowersss
s = "This is DATA Analysts/Data ScienCE Batch"
u = 0
l = 0
o = 0
for i in s:
    if i.isupper():
        u = u + 1
    elif i.islower():
        l = l + 1
    else:
        o = o + 1
print(l)
print(u)
print(o)


# In[40]:


def xyz(x):
    u = 0
    l = 0
    o = 0
    d = 0
    for i in x:
        if i.isupper():
            u = u + 1
        elif i.islower():
            l = l + 1
        elif i.isdigit():
            d = d + 1
        else:
            o = o + 1
    print("Lower = ",l)
    print("Upper = ",u)
    print("Others = ",o)
    print("Digit = ", d)


# In[41]:


s = input("Enter It : ")
xyz(s)


# In[44]:


fruits = ["Apple", "Pear", "Orange"]

for fruit in fruits:
    print(fruit)
print()


# In[50]:


d = "This is Dev"
for i in d:
    print(i)
    if i =='D':
        break


# In[51]:


d = "This is Dev"
for i in d:
    if i ==' ':
        break
    print(i)


# In[56]:


d = "This is Dev"
for i in range(len(d)):
    if d[i] =='D':
        break
    print(i,d[i])


# In[60]:


len(d)


# In[64]:


x = int(input("Enter Value For Table "))
for i in range(1,11):
    print(i,"*",x,"=",i * x )


# 

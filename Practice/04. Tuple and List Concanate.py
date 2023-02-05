#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=input("enter the value:")
for i in range(1,11):
    print(n,'x',i,'=',i*10)


# In[35]:


# Testing Buddy
a = ()
a1= (100,200,300,100,200)


# In[36]:


# type(a1)
# len(a1)


# In[37]:


a1.count(100)


# In[41]:


a1.index(300)


# In[43]:


for i in a1:
    print(i,end=" ")


# In[48]:


s = (500,200,300,200,200)
b=200
c=0
d=[]
for i in s:
    if i==b:
        c+=1
        d.append(i)
print(c)
print(d)


# In[50]:


s = (500,200,300,(1,2,3,4))
for i in s:
    print(i)
type(s)


# In[64]:


# Conconate tuples in one tuple and output in list convert to tuple
s = (500,200,300,(1,2,3,4),"a","b","c","d",[5,6,7])
x=[]
for i in s:
    if type(i)==int:
        x.append(i)
    elif type(i)==tuple:
        for j in i:
            x.append(j)
    elif type(i)==str:
        for k in i:
            x.append(k)
    elif type(i)==list:
        for l in i:
            x.append(l)
print("Normal Number tuple str list ",x)
c = tuple(x)
print("Conveted to Tuple",x)


# In[71]:


a=int(input("Enter a"))
b =int(input("Enter b"))
c =input("Enter +,-")
if c =='+':
    x=a+b
    print(x)
elif c =='-':
    x2=a-b
    print(x2)
else:
    print("Madddd")


# In[ ]:





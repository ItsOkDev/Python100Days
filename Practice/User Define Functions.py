#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add():
    a = 10
    b = 20
    c = a + b
    print(c)
add()


# In[3]:


def add(a,b):
    c = a + b
    print(c)
add(10,20)


# In[ ]:


1. varaible - "Storing the data"


# In[5]:


5%2
3%2
2%2


# In[7]:


b = 1
type(b)


# In[16]:


a = input("Enter Any ").title()
print("Hello You " + a + " Your Nice!")


# In[18]:


a = ("Health is Wealth")
a.replace("Health", "Honey")


# In[20]:


b = [1,2,3,4]
x = []
b.append(x)
print(x)


# In[ ]:





# In[28]:


x = {1,2,3,4}
x.update([11,22,33])
print(x)


# In[47]:


# Write your code below this line 👇
p = int(input("Enter Physics marks "))
c = int(input("Enter Chem marks "))
m = int(input("Enter Maths marks "))
t = (p+c+m)/3
if (p>=35 and c>=35 and m>35):
    print("You Are TOPPER BRO",t)
elif (p>=35 and c>=35 and m<=35):
    print("Maths FAIL Bhai",t)
elif (p<=35 and c>=35 and m>=35):
    print("PHY FAIL Bhai",t)
else:
    print("CHEM Fail Bhai",t)
print("HEY MAD YOUR PERCENT IS :", t ,"%")


# In[ ]:





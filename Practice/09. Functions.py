#!/usr/bin/env python
# coding: utf-8

# In[15]:


def add():
    x = 10
    y = 20
    c = x + y
    print(c)
add()


# In[14]:


# Defining Function one time
def disp():
    name = "GeekyShows"
    print("Welcome to", name)
# Calling Function as many time as we need
disp()


# In[17]:


#Defining a Function with Parameter
def add(b):
    a = 10
    c = a + b
    print(c)
#Calling a Function with Argument
add(5)


# In[20]:


#Defining a Function with Parameter
def add(y):
	x = 10.2334
	print(x+y)
	print(f"Formatted Output {x+y:5.2f}")
	
#Calling a Function with Argument
add(20)


# In[41]:


def sub(a,b): # Its is Subtraction 
    c = a - b
    print(c)
def div(a,b): #Its a Basic Dicvison
    c = a/b
    print(c)
def div_floor(a,b): #Floor It will take round figure
    c = a//b
    print(c)
def Modulos(a,b): # Modulo Means taking Remainder 
    c = a%b
    print(c)
def mul(a,b): #Its Multiplxn
    c = a * b
    print(c)
def add(a,b): #Its ADditiom
    c = a + b
    print(c)
def exponent(a,b): #Its an Exponent
    c = a**b
    print(c)


# In[43]:


mul(30,20)
div(30,20)
div_floor(30,20)
Modulos(30,20)
sub(30,20)
add(30,20)
exponent(3,2)


# In[56]:


def eveodd(n=10): #Its an Default value
    if n%2==0:
        print("Even")
    else:
        print("Odd")
eveodd()


# In[54]:


eveodd(3) 


# In[66]:


s = [1,2,3,4,6,5,4,3,2]
s.sort()
print(s)


# In[64]:


s = [1,2,3,4,6,5,4,3,2]
s.sort(reverse=True) #Press Shift+tab For Reverse we take reverse as (True)
print(s)


# In[ ]:





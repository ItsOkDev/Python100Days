#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("****** Upper Function ******")
name = "geekyshows"
str1 = name.upper()
print(name)
print(str1)

print("****** Lower Function ******")
name = "GEEKYSHOWS"
str1 = name.lower()
print(name)
print(str1)

print("****** Swapcase Function ******")
name = "geekyshows"
str1 = name.swapcase()
print(name)
print(str1)

print("****** Title Function ******")
name = "hello geekyshows how are you"
str1 = name.title()
print(name)
print(str1)


# In[2]:


# Declaring and initializing Variable
# Individual
a = 10
b = 10.23
c = "GeekyShows"
d = 'GeekyShows'

# Multiple
e, f, g, h = 10, 10.23, "GeekyShows", 'GeekyShows'

# Multiple with same value
i = j = k = l = m = n = True

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(n)
print("$"*20)


# In[7]:


print("Hellow how Ru 'hi'")


# In[21]:


a = 'Hellow how Ru "hi"'
len(a)
type(a)


# In[22]:


a.lower()


# In[23]:


a.upper()


# In[24]:


a.title()


# In[42]:


x = "Hello Its Number"
x.islower()


# In[43]:


x.isupper()


# In[44]:


x.isdigit()


# In[45]:


x.isalpha()


# In[52]:


f="vgvgjvgv1115"


# In[53]:


f.isalpha()


# In[56]:


c=0
d=0
for i in f:
    if i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+1
print(c)
print(d)


# In[59]:


c=0
d=0
l=[]
l2=[]
for i in f:
    if i.isalpha():
        c=c+1
        l.append(i)
        
    elif i.isdigit():
        l2.append(i)
        
        d=d+1
print(c)
print(d)
print(l)
print(l2)


# In[84]:


print("Seperate Digit and Alphabhets ")
s = input("Enter The String ")
c=0
d=0
l=[]
l2=[]
for i in s:
    if i.isdigit():
        c=c+1
        l.append(i)
    elif i.isalpha():
        d = d+1
        l2.append(i)
print(l)
print(l2)


# In[91]:


h=input("Hello Enter Something...")
c1=0
c2=0
h1=[]
h2=[]
for i in h:
    if i.isdigit():
        c1=c1+1
        h1.append(i)
    if i.isalpha():
        c2=c2+1
        h2.append(i)
print(h1)
print(h2)


# In[95]:


a = int(input("enter"))
for i in range(1,11):
    print(a,"x",i,"=",i*a)


# In[96]:


print("****** isupper Function ******")
name = "GEEKYSHOWS"
str1 = name.isupper()
print(name)
print(str1)

print("****** islower Function ******")
name = "geekyshows"
str1 = name.islower()
print(name)
print(str1)

print("****** istitle Function ******")
name = "Hello Geekyshows How Are You"
str1 = name.istitle()
print(name)
print(str1)


# In[97]:


print("****** isdigit Function ******")
name = "342343"
str1 = name.isdigit()
print(name)
print(str1)

print("****** isalpha Function ******")
name = "GEEKyshows"
str1 = name.isalpha()
print(name)
print(str1)

print("****** isalnum Function ******")
name = "GEEKyshows2343"
str1 = name.isalnum()
print(name)
print(str1)


# In[99]:


print("****** isspace Function ******")
name = "  "
str1 = name.isspace()
print(name)
print(str1)


# In[101]:


n = "HEllo Dev"
old="HEllo"
new="New"
xyz = n.replace(old, new)
print(n)
print(xyz)


# In[106]:


n = "Hello-Oyy-nice"
str = n.split('-')
print(str)


# In[109]:


n = ('Hello', 'HOW', 'RU')
str = "-".join(n)
print(str)


# In[ ]:





# In[107]:


print("****** join Function ******")
name = ('Hello', 'How', 'Are', 'You')
str1 = "_".join(name)
print(name)
print(str1)


# In[ ]:


print("****** replace Function ******")
name = "Geekyshows"
old = "Geeky"
new = "New"
str1 = name.replace(old, new)
print(name)
print(str1)

print("****** split Function ******")
name = "Hello-how-are-you"
str1 = name.split('-')
print(name)
print(str1)

print("****** join Function ******")
name = ('Hello', 'How', 'Are', 'You')
str1 = "_".join(name)
print(name)
print(str1)


# In[110]:


print("****** startswith Function ******")
name = "Hi How are you"
str1 = name.startswith('Hi')
print(name)
print(str1)

print("****** endswith Function ******")
name = "Thank you Bye"
str1 = name.endswith('Bye')
print(name)
print(str1)


# In[ ]:





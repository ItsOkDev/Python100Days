#Day 30/01/2023

# Tables Padh LE Bhai
n = int(input("Enter the Number "))
for i in range (1, 10+1):
    print(n, "*",i,"=",i*n)


# In[15]:
# def = Keyword and Mry() = is Function
# An argument is the value passed to the function. Down
# An attribute is a variable or method of a class.
def mry():
    print("Even Buddy")
mry()


# In[20]:
def mry(x):
    if x % 2 ==0:
        print("Even")
    else:
        print("ODD")
mry(7)


# In[ ]:
# Only one argument is Used
def add(a,b):
    print(a+b)
add(1)


# In[38]:
def powr(a=2):
    print(a**2)
powr()


# In[42]:
# Positional Argument
def sub(a,b):
    print(a-b)
sub(b=2, a=1)


# In[45]:
# *arg and **key arg
def mul(*arg):
    print(arg)
mul(4,3,2,2)


# In[52]:
def mul(*x):
    print(x)
mul(1,1,3)
# if star removed
# TypeError: mul() takes 1 positional argument but 3 were given


# In[59]:
def mul(*arg):
    for i in arg:
        print(i * 2, end=" ")
mul(1,2,3,4,5,6,7,8,9,10)


# In[74]:
def mul(*arg):
    c = 1
    for i in arg:
        c = c * i
    print(c)
mul(1,2,3)


# In[80]:
def powr(a):
    print(a**2)
n = int(input("Enter Number "))
powr(n)


# In[95]:
d = int(input("Enter Num "))
powr(d*5)


# In[92]:
def powrs(a):
    '''This is Power sqr Program it take one value output'''
    print(a**2)
n = int(input("Enter Number "))
powr(n)


# In[94]:
powrs(5)


# In[ ]:
str()

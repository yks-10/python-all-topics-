'''
Beginner (Foundations)
'''


# 1. Variables & data type

roll_no = 12        # int
average = 97.9      # float
complex_a = 2+5j    # complex - real imag
print(complex_a.real)
print(complex_a.imag)

name = "Yogesh"     # string
name_size = len(name) # len() method
print(name_size)
print(name.upper())
print(name.lower())
print(name.title())
print(name.islower())
print(name.isupper())
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())
print(name.isspace())
print(name.isnumeric())
print(name.capitalize())
print(name.casefold())
print(name.swapcase())
print(name.__len__())
print(name.count('Y'))
print(name.__contains__('Y'))
print(name.__eq__("Yogesh"))
print(name.__ge__("Yogesh"))

#  bollen
value = None
if value:
    print("Yes")
else:
    print("No")

# type casting
value = "55678"
print(value)
print(int(value))
print(float(value))
print(list(value))
print(tuple(value))
print("".join(set(value)))

# operators
ramu, somu = 0,0
ramu +=2
somu += 3
somu = ramu-somu
print(somu, ramu)
print(0*5)
print(0**5)
print("0^5", 0^5)
print(0%5)
print(0//5)
print(11/5)
print(11//5)

# assignment operator
x,y = 5, 4
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
x+=1
y-=1
print("x is",x,"y is",y)
print(f"y is {y}")
x%=y
print(x)
x/=y
print(y)

# membership operator | in
nick_name, name = "yks", "yogesh"
print(nick_name in name)
print(nick_name not in name)

# identity operator
# is checks the memory  == checks the values

print("IDENTITY")
x = 4
y=4
x1 = x
y1 = 4
print(x is x1)
print(x is y)
print(x is not y1)
print(x==y1)

# input
# name = input("What is your name?")
# mark = int(input("What is your mark?"))
# list_mark = list(map(int, input().split()))
# print(list_mark)

x = 2
print(f"value is {x:.10f}")

# conditional statement

x, y = 2, 4
if x==y:
    print("YES")
elif x!=y:
    print("NO")
else:
    print("YES")

# looping
# for while | break, continue, pass
print([ i for i in range(10) ])

while x!=y:
    print(x)
    x+= 1

# data structure
roll_no =[1,2,3,3,] # list
print(roll_no)

roll_no.append(7)
roll_no.sort()
print(roll_no)
roll_no.extend([1,2,3,4,5,6])
print(roll_no)
print(sorted(roll_no))
print(roll_no.index(7))
print(7 in roll_no)
print(roll_no.count(7))
print(set(roll_no))
roll_tuple = (1,2,3,4) # tuple
roll_set = {1,2,3,4}
roll_dict ={"abi":1,"bay":2,"cat":3}
print(roll_dict.values())
print(roll_dict.items())
print(list(roll_dict.keys()))


# Function

def add(a=20,b=10):
    return a+b
print(add(1,2))
print(add(2))


def subtract(*args):
    return args[0]-args[1]
print(subtract(2,2))

def multiply(**kwargs):
    return kwargs['x']*kwargs['y']
print(multiply(x=10,y=10))


def add(x,y,**kwargs):
    return x+y+kwargs['x1']
print(add(1,2,x1=2000))


def validation(x):
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x<=0:
        raise ValueError("x must be positive")
    return x

try:
    validation(5)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("Yey")
finally:
    print("Yey")


'''
Intermediate (Core Programming)
'''

# List comprehension
x =  [i for i in range(10)]

# set comprehension
y = {i for i in "maddy"}

#dictonary
d = {'a':62,'b':63,'c':64}
d = {j:i for i, j in d.items()}
print(d)

# Nested DS

# list of list
x = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

# list of dict
x =[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6},{'a':7,'b':8,'c':9}]

# dict of list
x = {"roll_no":[1,2,3,4], "name":["yks","yogesh","krishnan"]}



# Function

# recursion function calls itself until reaches it base condition
def add(n):
    if n==0:
        return 0
    else:
        return add(n-1)

print(add(10))

# *args
def display(*numbers):
    for i in numbers:
        print(i)
    return sum(numbers)
print(display(1,2,3))

# **kwargs
def func_kwargs(**kwargs):
    x = kwargs['x']
    y =  kwargs['y']
    return x+y
print(func_kwargs(x=100, y=200))

# lambda function
increment = lambda x: x+1
result = increment(1000)
print(result)


#  map applies for all iter
nums =[1,2,3]
x = list(map(lambda x: x**2, nums))
print(x)

# filters the values based on condition
nums = [1,2,3,4,5,6,7]
x = list(filter(lambda x: x%2==0, nums))
print(x)

# reduces
'''
    function from functools
    accept 2 args 
    (a iter, 1 optional may be intial value )
    return single value output 
'''
from functools import reduce
nums = [1,2]
x = reduce(lambda a,b: a+b, nums)
print(x)


# string manipulation: slicing, formating, regex
text = "yks"
print(text[0:1])

# formating
print(f"text {x}", 10)
print("heelo {}".format("hello"))



with open("yes.txt", 'r') as file:
    text = file.read()
    file.seek(0)

    text = file.readlines()
    for line in text:
        print(line)


# OS
import os

cwd = os.getcwd()
print(os.getcwd())
print(os.getcwd())
path = os.path.join(cwd,'yes.txt')
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.getsize(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.stat(path))
print(os.access(path, os.W_OK))
print(os.path.exists(path))



# pathlib

print('pathlib')

from pathlib import Path

cwd = Path(path)
print(path)

# Modules & Packages
'''
    module | single python(.py) file with reusable code 
    package | folder with __init__ and multiple module 
'''

# custom package
'''
    pyproject.toml | setuptools , wheel 
    setup.py | setup( name , version, desc, author, 
        packages, install_requirements , python_required )
'''

# virtual env python -m venv venv

# Exception Handling

try:
    x = 12/2
except TypeError as e:
    print("type error", e)
except ZeroDivisionError as e:
    print("division by zero")
else:
    print("Result",x)
finally:
    print("error handling")


try:
    x = 0/0
except (TypeError, ZeroDivisionError) as e:
    print(e)


# custom exception

class EnaError(Exception):
    pass

def validation(x):
    if not isinstance(x, int):
        raise EnaError("x must be an integer")
    return x

def add(a):
    try:
        return 1+validation(a)
    except EnaError as e:
        print(e)
print(add("1"))


# chain exception
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("coverstion failed") from e


# class and object | blueprint and instance
from datetime import time


class Student:

    def __init__(self, name, age):  # __init_ constructor  | 'name' attribute
        self.name = name
        self.age = age

    def details(self):  # function inside the class called method
        return f"{self.name} is {self.age} years old"

obj = Student("John", 18)
print(obj.details())

class Teacher(Student): # inheritance of student class
    def __init__(self, name, age):
        super().__init__(name, age)

obj = Teacher("John Paul", 18)
print(obj.details())


# polymorphism
# many forms | same method name different behaviour across class
class Cow:
    def sound(self):
        return "maaaaa"

class Cat:
    def sound(self):
        return "mew"

class Dog:
    def sound(self):
        return "woof"

for sound in (Dog(), Cat(), Cow()):
    print(sound.sound())


# Encapsulation |restrict direct access to attribute _protected and __private
class Bank:
    def __init__(self,name,balance, age):
        self.name = name # public attribute
        self.__balance = balance # private attribute
        self._age = age
    def __len__(self):   # Dunder Magic method
        return self.__balance

    def display(self):
        return f"{self.name} is ${self.__balance}"
obj = Bank("John", 1800, 10)
print(obj.name)
print(obj._age)
print(len(obj))

# print(obj.__balance)

# iter | next
x = [1,2,3,4,5]
it = iter(x)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Generator
'''
special function that returns iters 
memory efficiency | lasy evaluation 
produces one value at a time
'''

def simple_generator():
    yield 1
    yield 2
    yield 3
x = simple_generator()
print(x)
for i in x:
    print(i)


# generator expression
generator_expression = (i for i in range(10))
print(generator_expression)
for i in generator_expression:
    print(i)


def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")

counter = countdown(3)
print(next(counter))
print(next(counter))
print(next(counter))


# context manger
'''
is a object defines what happen at beginning and of the with 
ensure setup and cleanup operations automatically even error occurs 
__entry__(self) 
__exit__(self, exc_type, exc_value, exc_traceback)
from contextlib import contextmanager
'''

with open('yes.txt', 'r') as file:
    text = file.read()
    print(text)

    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line)

def generator_context():
    with open('yes.txt', 'r') as file:
        for line in file:
            yield line.strip()

generator_context = generator_context()
print(next(generator_context))
print(next(generator_context))


# decorator

'''
@wraps | preserve original function attributes
'''
import time
def time_cal(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

@time_cal
def add(x):
    return 10 + x
print(add(1))


def cal_decorator(cls):
    def __str__(self):
        return f"{self.__class__.__name__}"

    cls.__str__ = __str__
    return cls

@cal_decorator
class Student:
    pass

obj = Student
print(obj)


# math
'''
    sqrt 
    pow  
    abs 
    
    
    ceil 
    floor 
    trunc
    
    factorial
    comb
    per 
    
    
    math.pi
    
    sin
    cos
    tan
    
    radiant 
    degrees
    
    asin
    acos 
    atan 
    
    sinh
    cosh
    tanh
    
    log 
    log2 
    
    infi
    nan 
'''

# random
import random

print(random.random())
print(random.randint(0,100))
print(random.uniform(0,100))
print(random.gauss())

x = ['hello', 'world', 'hi']

print(random.choices(x))

weight =[1,3,2]
print(random.choices(x, weight))
print(random.sample(x, 2))
print(random.sample(range(10000), 5))

print(random.shuffle(x))

random.seed(1) # reproduce results

# datetime
from datetime import timedelta, datetime, timezone

print(datetime.now())
print(datetime.today())
print(datetime.now(timezone.utc))

x=datetime.today()
print(x.year, x.month, x.day)
print(x.hour, x.minute, x.second, x.microsecond)
print(x.weekday())
print(x.isoweekday())


future = datetime.today() + timedelta(days=5, hours=1)
print(future.year, future.month, future.day)

# Collections
from collections import Counter
x = [1,2,3,4,5,1,2,3,4]
y = Counter(x)
print(y)

from collections import deque # double ended que
dq = deque([1,2,3,4,5,6,7])
dq.append(8)
print(dq)
dq.appendleft(0)
print(dq.pop())
print(dq.popleft())

print(dq.rotate(2))
print(dq)
print(dq.rotate(-2))
print(dq)

dq.extend([8,9])
print(dq)
dq.extendleft([-1,0.0])
print(dq)

dq1 = deque(maxlen=3)
dq1.append(1)
print(dq1)
dq1.append(2)
dq1.append(3)
dq1.append(4)
print(dq1)

from collections import OrderedDict

ord_dic = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ord_dic)
print(ord_dic.items())
print(ord_dic.keys())
print(ord_dic.values())
print(ord_dic.popitem(last=False))
print(ord_dic.popitem(last=True))

from collections import namedtuple

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5, 'e': 6}

chain = ChainMap(dict1, dict2, dict3)
print(chain)

print(list(chain.items()))
print(list(chain.keys()))
print(list(chain.values()))
print(chain['b'])
chain['f']=7
chain.new_child({'g':8})
print(chain)




import asyncio

async def test():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

async def main():
    await asyncio.gather(test(), test())

print(asyncio.run(main()))
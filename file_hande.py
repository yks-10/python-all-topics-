'''
    r : read
    w : write
    x : craete file
    a : append
    r+ : read & write
    rb : read binary mode
    wb : write binary mode
    ab : append binary mode
'''

import json 
def file_check(path):
  if not path.endswith('.json'):
    raise TypeError("Json file only accepted")
    
  try:
    with open(path, 'r') as file:
      content = file.read.strip()
      if not content:
        raise ValueError("Empty File")
      data = json.load(content)
      return content 
  except FileNotFoundErr:
    print("file not found")
  except json.JSONDecodeError:
    print("json format ")
  except Exception as e:
    print("Unexpected error")
    
    
  if not path.endswith(".json"):
    raise TypeError("")
    
  with open('test.text', 'r') as file:
    content = file.read.strip()
    if not content:
      raise ValueError("Empty File")
    
    
from yes1 import text

with open("yes.txt", "r") as file: # with is context manager
    content = file.read()
    print(content)

    file.seek(0)
    for line in file:
        print(line.strip())

    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line.strip())




import time

def time_cal(func):
    def wrapper(*args,**kwargs):
        start =time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper

@time_cal
def add(a,b):
    return a+b
add(1,2)

# @receiver(pre_save, sender=User)
# @receiver(post_save, sender=User
# @receiver(m2m_changes, sender=Profile.sender.through)









'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int
    mark:float

@app.get("/")
def health_check():
    return {"succes": "Server is running"}
'''

# uvicorn filename.py:app --reload

import threading

def hello():
    print("Hello")

def add(a,b):
    thread = threading.Thread(target=hello)
    thread.start()
    thread.join()
    return a+b
print(add(1,2))



def palindrome(text):
    text  = "".join(i for i in text if i.isalnum())
    if text == text[::-1]:
        return True
    else:
        return False
print(palindrome("rac a car"))


from collections import Counter


def first_non_repetitive_character(text):
    frequency = Counter(text)
    print(frequency)
    for i, character in enumerate(text):
        print(i, character)
        if frequency[character] == 1:
            return character
    return 0
print(first_non_repetitive_character("race a car"))

x = []
for i in "race a car":
    if i not in x:
        x.append(i)
    else:
        x.remove(i)
print(x[0])




# import dis
#
# def combine_strings(name):
#     a = "Hello, " + name + "!"
#     b = f"Hello, {name}!"
#     return a, b
#
# dis.dis(combine_strings)


import threading, time

def cpu_task():
    count = 0
    for _ in range(100_000_000):
        count += 1

start = time.time()
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)
t1.start(); t2.start()
t1.join(); t2.join()
print("Threading Time:", time.time() - start)


from multiprocessing import Process
import time

def cpu_task():
    count = 0
    for _ in range(100_000_000):
        count += 1

start = time.time()
p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)
p1.start(); p2.start()
p1.join(); p2.join()
print("Multiprocessing Time:", time.time() - start)

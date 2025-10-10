# import threading

# def worker(name):
#     print(f"Thread {name} running")

# # Method 1: Using Thread class
# t = threading.Thread(target=worker, args=('A',))
# t.start()
# t.join()

# # Method 2: Subclassing Thread
# class WorkerThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#     def run(self):
#         print(f"Thread {self.name} running")

# t = WorkerThread("Yogesh")
# t.start()
# t.join()

import threading

rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            print(n)
            recursive_function(n - 1)

t = threading.Thread(target=recursive_function, args=(3,))
t.start()
t.join()
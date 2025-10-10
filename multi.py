from multiprocessing import Process, Queue, Pipe, \
    Value, Array, Pool

def worker(name):
    print(f"Worker {name} running")

def producer(q):
    q.put("data")

def consumer(q):
    data = q.get()
    print(data)

def sender(conn):
    conn.send("message")
    conn.close()

def modifier(num, arr):
    num.value = 10
    for i in range(len(arr)):
        # print(arr[:])
        arr[i] = -arr[i]

def square(x):
    return x*x

if __name__ == '__main__':
    p = Process(target=worker, args=('A',))
    p.start()
    p.join()

    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    parent_conn, child_conn = Pipe()
    p3 = Process(target=sender, args=(child_conn,))
    p3.start()
    print(parent_conn.recv())
    p.join()

    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=modifier, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])

    with Pool(processes=4) as pool:
        results = pool.map(square, range(10))
        print(results)
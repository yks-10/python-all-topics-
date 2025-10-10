# Multiprocessing in Python: A Detailed Explanation

Multiprocessing allows Python to run multiple processes in parallel, bypassing the Global Interpreter Lock (GIL) that limits threading in Python.

## How It Works

### **1. Process Creation**

When you create a new process, Python actually spawns a completely separate Python interpreter instance:

```python
from multiprocessing import Process

def worker(name):
    print(f"Worker {name} running")

if __name__ == '__main__':
    p = Process(target=worker, args=('A',))
    p.start()
    p.join()
```

**What happens internally:**
- The operating system creates a new process using `fork()` (Unix) or `spawn()` (Windows)
- Each process has its own Python interpreter and memory space
- Processes are completely isolated from each other

### **2. Memory Model**

Each process has its own:
- **Memory space**: Variables aren't shared between processes
- **GIL**: Each process has its own GIL, so true parallelism is possible
- **Resources**: File descriptors, network connections, etc.

```python
# This demonstrates memory isolation
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")

if __name__ == '__main__':
    p1 = Process(target=increment)
    p2 = Process(target=increment)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Main counter: {counter}")  # Still 0!
```

### **3. Start Methods**

Python offers three ways to start processes:

**spawn** (default on Windows/macOS):
- Starts a fresh Python interpreter
- Slower but safer
- Parent process data not inherited

**fork** (default on Unix):
- Copies the entire parent process
- Faster but can cause issues with threads
- Child inherits parent's memory state

**forkserver**:
- Hybrid approach
- Starts a server process that forks children

```python
import multiprocessing as mp
mp.set_start_method('spawn')  # Set explicitly
```

### **4. Process Communication**

Since processes don't share memory, you need Inter-Process Communication (IPC):

**Queues** (thread and process safe):
```python
from multiprocessing import Process, Queue

def producer(q):
    q.put("data")

def consumer(q):
    data = q.get()
    print(data)

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

**Pipes** (one-to-one communication):
```python
from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("message")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
```

**Shared Memory** (for efficiency):
```python
from multiprocessing import Process, Value, Array

def modifier(num, arr):
    num.value = 3.14
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd' = double
    arr = Array('i', range(10))  # 'i' = integer
    
    p = Process(target=modifier, args=(num, arr))
    p.start()
    p.join()
    
    print(num.value)  # 3.14
    print(arr[:])  # [0, -1, -2, ...]
```

### **5. Process Pools**

The `Pool` class manages multiple worker processes:

```python
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        # Map function across multiple inputs
        results = pool.map(square, range(10))
        print(results)
```

**Pool methods:**
- `map()`: Blocks until all results ready
- `map_async()`: Returns immediately with AsyncResult
- `apply()`: Single function call (blocking)
- `apply_async()`: Single function call (non-blocking)
- `starmap()`: Like map but unpacks arguments

### **6. Process Lifecycle**

```python
p = Process(target=func)
p.start()      # OS creates new process
p.is_alive()   # Check if running
p.join()       # Wait for completion
p.terminate()  # Force kill (SIGTERM)
p.kill()       # Force kill (SIGKILL)
p.exitcode     # Exit status
```

### **7. Synchronization Primitives**

**Lock**:
```python
from multiprocessing import Process, Lock

def worker(lock, num):
    lock.acquire()
    try:
        print(f"Process {num}")
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    processes = [Process(target=worker, args=(lock, i)) for i in range(5)]
    for p in processes: p.start()
    for p in processes: p.join()
```

**Semaphore, Event, Condition**: Similar to threading equivalents but work across processes.

### **8. Key Considerations**

**Overhead:**
- Process creation is expensive (10-100ms)
- Data serialization (pickling) for IPC adds overhead
- Use processes for CPU-bound tasks, not I/O-bound

**Pickling Requirements:**
- All data passed between processes must be picklable
- Functions must be defined at module level (not in `__main__`)
- Lambda functions don't work with default pickler

**When to Use:**
- CPU-intensive computations
- Avoiding GIL limitations
- True parallelism needed
- Task isolation required

**When NOT to Use:**
- I/O-bound tasks (use `asyncio` or threading)
- Low-latency requirements
- Frequent inter-process communication
- Large data sharing needed

The multiprocessing module essentially lets Python sidestep the GIL by running separate Python interpreters, enabling true parallel execution at the cost of higher overhead and complexity in sharing data.
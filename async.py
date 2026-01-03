# import asyncio
'''
    sleep()
    get_event_loop()
    run()
    create_task()
    gather()
    wait_for( , timeout=2)
'''


# async def fetch_data():
#     global count 
#     count += 1
#     await asyncio.sleep(2)
#     print("Wait 2 seconds")
#     return "data feteched"

# async def main():
#     start = asyncio.get_event_loop().time()
#     print("Start")
#     await asyncio.gather(fetch_data(), fetch_data())
#     #print("Total time", asyncio.get_event_loop().time() - start)
#     print("DOne")
# asyncio.run(main())


# import asyncio

# async def greet():
#     print("START")
#     await asyncio.sleep(2)
#     print("END")


# asyncio.run(greet())

# asyncio.create_task(), asyncio.gather()

# import asyncio

# async def process(i):
#     await asyncio.sleep(i)

# async def main():
#     task_1 = asyncio.create_task(process(1))
#     await task_1 


# async def main():
#     start = asyncio.get_event_loop().time()
#     await asyncio.gather(
#         process(1), 
#         process(2),
#         process(3),
#         process(4),
#         process(5),
#     )
#     print("total time", asyncio.get_event_loop().time() - start)


# asyncio.run(main())



import asyncio, random 

async def task(i):
    await asyncio.sleep(i)
    return f"Task {i} s done"

async def main():
    tasks =[
        asyncio.wait_for(task(random.randint(1,5)), timeout=3)
        for _ in range(3)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"task {i} failed:{type(result).__name__}")
        else:
            print(f"task {i} completed: {result}")

asyncio.run(main())

# import asyncio, random

# async def task(i):
#     await asyncio.sleep(i)
#     return f"Task {i}s done"

# async def main():
#     tasks = [
#         asyncio.wait_for(task(random.randint(1, 5)), timeout=3)
#         for _ in range(3)
#     ]

#     results = await asyncio.gather(*tasks, return_exceptions=True)
#     for i, result in enumerate(results, 1):
#         if isinstance(result, Exception):
#             print(f"Task {i} failed: {type(result).__name__}")
#         else:
#             print(f"Task {i} completed: {result}")

# asyncio.run(main())

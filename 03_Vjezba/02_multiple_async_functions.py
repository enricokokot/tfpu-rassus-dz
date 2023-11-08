import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(2)
    print("Task 1: End")

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(3)
    print("Task 2: End")

async def main():
    # Create asynchronous tasks
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    
    # Execute tasks concurrently using asyncio.gather()
    await asyncio.gather(task_1, task_2)

# Run the main function
asyncio.run(main())

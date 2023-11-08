# Write 2 functions : 
# a ) async def timeout_example()
# b ) async def function_to_call()
# Edit the timeout_example() function so that it times out after 3 seconds
# and raises a "TimeoutError" if it doesn't complete in time
# Edit the function_to_call() function so that it executes longer than 3 seconds
# to trigger the "TimeoutError" in the timeout_example() function
import asyncio

async def timeout_example():
    try:
        await asyncio.wait_for(async_function(), timeout=3)
    except asyncio.TimeoutError:
        print("Async function timed out!")

async def async_function():
    await asyncio.sleep(5)

asyncio.run(timeout_example())

import time
import asyncio


def sync_task(name):
    print(f"Starting {name}")
    time.sleep(3)  # blocking operation
    print(f"Finished {name}")
    return f"{name} result"



async def main():
    result1, result2 = await asyncio.gather(
        asyncio.to_thread(sync_task, "Task 1"),
        asyncio.to_thread(sync_task, "Task 2"),
    )
    print(result1)
    print(result2)



asyncio.run(main())
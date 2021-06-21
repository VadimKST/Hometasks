import random
import asyncio

warehouse = []

max_elements = 10


def is_overflow():
    return len(warehouse) >= max_elements


def is_underflow():
    return len(warehouse) == 0


async def producer():
    while True:
        x = random.randint(a=1, b=10000)
        print('Producer number {}'.format(x))

        if not is_overflow():
            warehouse.append(x)

        else:
           print("Overflow. Producer waiting")

        await asyncio.sleep(random.random() * 2.0)


async def consumer():
    while True:
        if not is_underflow():
            x = warehouse.pop(0)
            print('Consumer number {}'.format(x))
        else:
            print("Underflow. Consumer waiting")

        await asyncio.sleep(random.random() * 5.0)


async def main():
    task1 = asyncio.create_task(producer())
    task2 = asyncio.create_task(consumer())

    await task1
    await task2

asyncio.run(main())

import uvloop
import asyncio
import datetime
from asyncio import AbstractEventLoop

import colorama
import random
import time

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

def main():
    # Create the asyncio loop
    loop: AbstractEventLoop = asyncio.get_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data = asyncio.Queue()  # maybe a better data structure?

    # Run these with asyncio.gather()
    # wait time 0
    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data)
    )
    loop.run_until_complete(task)
    # this will have less parallelism, more time waiting
    # task2 = asyncio.gather(
    #     generate_data(10, data),
    #     generate_data(10, data),
    #     process_data(20, data)
    # )
    # loop.run_until_complete(task2)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx
        # Use queue
        work = (item, datetime.datetime.now())
        # data.append(work)
        await data.put(work)

        print(colorama.Fore.YELLOW + " -- generated item {}".format(idx), flush=True)
        # Sleep better
        # time.sleep(random.random() + .5)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        # Use queue
        # item = data.pop(0)
        # if not item:
        #     time.sleep(.01)
        #     continue
        # item1 =  data.get()
        # item1 is a coroutine, if we don't await data.get()
        item = await data.get()
        # putting await before a coroutine, waits for coroutine to finish and grabs
        # out it's return value, now item is a tuple

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        # Sleep better
        # time.sleep(.5)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()
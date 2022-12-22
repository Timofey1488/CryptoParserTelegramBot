import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(2)


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        current_datetime = datetime.datetime.now()
        print("Loop: {} Time: {}".format(num, current_datetime.minute))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))

loop.run_forever()

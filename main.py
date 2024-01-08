import threading as tr
import time
import asyncio
import smtplib

# def infinte_loop():
#     while 1 == 1:
#         pass
#
#
# def my_name():
#     print('_-Name-_')
#
#
# t1 = tr.Thread(target=infinte_loop)
# t2 = tr.Thread(target=my_name)
#
# t1.start()
# t2.start()


# def a():
#     value = b()
#     print(value)
#
#
# def b():
#     time.sleep(5)
#     return 5
#
#
# a()

# loop = asyncio.new_event_loop()
#
# task1 = asyncio.sleep(2)
#
# loop.run_until_complete(task1)
#
# print('Done')


# async def square(num):
#     return num * num
#
#
# async def master():
#     x = await square(5)
#     print(x)
#
#     y = await square(10)
#     print(y)
#
#     z = x + y
#     print(z)
#
#
# asyncio.run(master())

# start = time.time()

# Sync
# def sync_get_movie_ticket():
#     time.sleep(3)
#     print('Got the movie tickets')
#
#
# def sync_like_instagram_photo():
#     time.sleep(1)
#     print('Finished Instagram')
#
#
# def sync_head():
#     sync_get_movie_ticket()
#     sync_like_instagram_photo()
#
#
# sync_head()
# print('The time of execution: ', int(time.time() - start), 'sec')

# ____________________________________________________________________--Async
# async_start = time.time()
#
#
# async def async_get_movie_ticket():
#     await asyncio.sleep(3)
#     print('Got the movie tickets')
#
#
# async def async_like_instagram_photo():
#     await asyncio.sleep(1)
#     print('Finished Instagram')
#
#
# async def async_head():
#     t1 = asyncio.create_task(async_get_movie_ticket())
#     t2 = asyncio.create_task(async_like_instagram_photo())
#     await t1
#
#
# asyncio.run(async_head())
# print('ASYNC The time of execution: ', int(time.time() - async_start), 'sec')

start = time.time()


# Slow (Sync)
# def fetch_file():
#     print('Starting to fetch a file')
#     time.sleep(1)  # Simulate time taken download a file
#     print('Fetching finished')
#
#
# def chief():
#     print('Staring master')
#     fetch_file()
#     fetch_file()
#     fetch_file()
#     print('Main completed')
#
#
# chief()
# end = time.time()
# print('Execution time is: ', int(end - start))

# Fast(Async)
# async def fetch_file():
#     print('Starting to fetch a file')
#     await asyncio.sleep(1)  # Simulate time taken download a file
#     print('Fetching finished')
#
#
# async def chief():
#     print('Staring master')
#     await asyncio.gather(
#         fetch_file(),
#         fetch_file(),
#         fetch_file())
#     print('Main completed')
#
#
# asyncio.run(chief())
# end = time.time()
# print('Execution time is: ', int(end - start))


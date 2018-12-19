import asyncio,random
async def random_inc(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        await asyncio.sleep(sleep_secs) #耗时操作
        print('inc {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

async def random_inc_larger(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        await asyncio.sleep(sleep_secs) 
        print('inc larger {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        random_inc(8),
        random_inc_larger(8),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()

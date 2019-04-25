import asyncio
from threading import Thread

loop = asyncio.new_event_loop()

def f(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

t = Thread(target=f, args=(loop,))
t.start()    

@asyncio.coroutine
def g():
    yield from asyncio.sleep(1)
    print('Hello, world!')

async def coro_func():
    await asyncio.sleep(1, 42)
    return "abc"

# loop.call_soon_threadsafe(asyncio.async, g())
future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
print("Wait for the result") ## this will run immediately
result = future.result() ## has to wait for result
print("result", result)
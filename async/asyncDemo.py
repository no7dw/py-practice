import asyncio

async def foo():
    print('in foo')
    await asyncio.sleep(1)
    print('explicit context switch to foo again')

async def bar():
    print('in bar')
    await asyncio.sleep(3)
    print('implicit context switch back to bar')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()


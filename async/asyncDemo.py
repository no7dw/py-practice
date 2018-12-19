import asyncio

async def foo(sec=1):
    print('in foo')
    await asyncio.sleep(sec)
    print('explicit context switch to foo again')
    return sec

async def bar(sec=3):
    print('in bar')
    await asyncio.sleep(sec)
    print('implicit context switch back to bar')
    return sec

loop = asyncio.get_event_loop()
# tasks = [loop.create_task(foo()), loop.create_task(bar())] # 简化成下方
tasks = [foo(), bar()] 
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)

# 使用gather 去获取 coroutine/future result
result = loop.run_until_complete(asyncio.gather(*[
    foo(),
    bar()
]))
for i in result:
    print(i)

loop.close()


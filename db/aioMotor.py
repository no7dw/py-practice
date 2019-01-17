import motor.motor_asyncio
import time
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

db=client['cashLoan']
col=db['userModelLog']

async def query(q):
    result = await col.find_one(q)
    #print(result)
    #return list(result)
    return result

async def insert(doc):
    result = await col.insert_one(doc)
    return result

async def update(q, new):
    result = await col.replace_one(q, new)
    return result

async def count(q):
    result = await col.count_documents(q)
    return result

async def delete(q):
    result = await col.delete_many(q)
    return result

# def promise(f):
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(f)
#     print("create task",task)
#     loop.run_until_complete(task)
#     print("run",task)
#     return task

# only run in main 
def promise2(task):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    # print("run",task)
    # loop.close()
    return task

async def patch_query():
    q = {'orderId':'5bf6d577ea5140000f0dc03c'}
    arrjob = []
    for i in list(range(0,1)):
        arrjob.append(query(q))
    print(len(arrjob))
    dones, pendings = await asyncio.wait(arrjob)

    for done in dones:    
        print(done.result())

async def main():
    q = {'orderId':'5bf6d577ea5140000f0dc03d'}

    # in async func you can call await
    c = await count(q)
    print("count before:", c)
    
    c = await insert({'orderId':'5bf6d577ea5140000f0dc03d', 'by':'wade'})
    print("r:", c)

    c = await count(q)
    print("count mid:", c)

    c =  await delete({'by':'wade'})
    print("delete:", c)

    c = await count(q)
    print("count final:", c)

    await patch_query()

s = time.time()

promise2(main())

e = time.time()

print(e-s)
#print(len(result),result[0])

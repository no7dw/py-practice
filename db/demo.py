import motor.motor_asyncio
import time
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

db=client['cashLoan']
col=db['userModelLog']

async def q(query):
    result = await col.find_one(query)
    #print(result)
    #return list(result)
    return result

async def main():
    arrjob = []
    query= {'orderId':'5bf6d577ea5140000f0dc03c'}
    for i in list(range(0,10000)):
        arrjob.append(q(query))
    print(len(arrjob))
    dones, pendings = await asyncio.wait(arrjob)

    for done in dones:    
        pass
        #print(done.result())

s = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
e = time.time()

print(e-s)

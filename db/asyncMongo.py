import pymongo
import time
import asyncio

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client['cashLoan']
col=db['userModelLog']

async def q(query):
    result = await col.find(query)
    #print(result)
    #return list(result)
    return result

async def main():
    arrjob = []
    query= {'orderId':'5bf6d577ea5140000f0dc03c'}
    for i in list(range(0,3000)):
        arrjob.append(q(query))
    print(len(arrjob))
    dones, pendings = await asyncio.wait(arrjob)
    
    #print(dones[1].result())

s = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
e = time.time()

print(e-s)
#print(len(result),result[0])

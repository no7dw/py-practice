import motor.motor_asyncio
import time
import asyncio
from aiomotorengine import connect, Document, StringField, IntFiled 

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

db=client['cashLoan']
col=db['userModelLog']

class UserModelLog(documents):
    __collection__ = 'userModelLog'    
    def __repr_(self):
        pass 

async def q(query):
    result = await UserModelLog.objects.find_one(query)
    #result = await col.find_one(query)
    #print(result)
    #return list(result)
    return result

async def main():
    arrjob = []
    query= {'orderId':'5bf6d577ea5140000f0dc03c'}
    for i in list(range(0,1000)):
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
#print(len(result),result[0])

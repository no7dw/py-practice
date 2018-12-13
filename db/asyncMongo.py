import pymongo
import time
import asyncio

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client['cashLoan']
col=db['userModelLog']

async def q(query):
    result = await list(col.find(query))
    print(result)
    return result

async def main():
    arr = []
    for i in list(range(0,3)):
        query= {'orderId':'5bf6d577ea5140000f0dc03c'}
        arr.append(q(query))
    print(len(arr))
    print(arr[1])

s = time.time()
asyncio.run(main())
e = time.time()

print(e-s)
#print(len(result),result[0])

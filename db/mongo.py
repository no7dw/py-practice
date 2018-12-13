import pymongo
import time


client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client['cashLoan']
col=db['userModelLog']

def q():
    query= {'orderId':'5bf6d577ea5140000f0dc03c'}
    for i in list(range(1,3000)):
        result = list(col.find(query))
        #print(i, result[0])
s = time.time()
q()
e = time.time()
print(e-s)
#print(len(result),result[0])

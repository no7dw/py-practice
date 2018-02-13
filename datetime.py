from datetime import datetime
print(datetime(2018,1,2,19,20))
dt=datetime.now()
print(dt)
print(dt.timestamp())
print(dt.strftime('%Y/%m/%d %H:%M'))

# python3 work
dt=datetime(2018,1,2,19,20)
dt.timestamp()
# error
print(dt+timedelta(days=1))

from walrus import Database

db = Database()
stream = db.Stream('stream-a')
msgid = stream.add({'message':'hello, stream world'})
msgid2 = stream.add({'message':'hello, stream world 2'})
msgid3 = stream.add({'message':'hello, stream world 3'})

messages = stream[msgid2:]

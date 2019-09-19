import mysql.connector
import config

mydb = mysql.connector.connect(
  host = config.mysql_host,
  user = config.mysql_user,
  passwd = config.mysql_passwd,
  database = config.mysql_database
)

def insert(content):
  mycursor = mydb.cursor()
  sql = "DELETE FROM addressBook"
  mycursor.execute(sql)

  sql = "INSERT INTO addressBook (name, address) VALUES (%s, %s)"
  
  mycursor.executemany(sql, content)

  mydb.commit()

  print(mycursor.rowcount, "was inserted.")

if __name__ == '__main__':
  content = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
  ]
  insert(content)
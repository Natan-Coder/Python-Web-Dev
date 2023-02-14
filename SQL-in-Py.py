import sqlite3

connect = sqlite3.connect('data.db')

# connect.execute("DROP TABLE IF EXITS CUSTOMER")
connect.execute('''CREATE TABLE CUSTOMER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL);''')

connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1, 'Nathan', 27)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (2, 'George', 32)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (3, 'Prince', 33)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (4, 'Jerry', 36)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (5, 'Phyllis', 54)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (6, 'Harry', 21)")
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (7, 'Samantha', 29)")

all_data = connect.execute('''SELECT * FROM CUSTOMER''')
for row in all_data:
    print(row)

connect.close()
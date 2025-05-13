import sqlite3
# 
# # connect to a Sqlite Database (or create a new one)
# conn = sqlite3.connect("SW12/testDB.db")
# 
# # get a cursor object to interact with the Database
# cursor = conn.cursor()
# 
# # write query
# sql_querry = """
# SELECT id,name
# FROM test_table
# WHERE id != 1
# """
# # execute querry
# cursor.execute(sql_querry)
# # to read out the answer, if any -> iterate through the cursor
# for row in cursor:
#     if input("Do you want to see the next row? (y/n)") == "y":
#         print(row) # print Answer, row by row
# 
# conn.close()

conn = sqlite3.connect("SW12/testDB.db")

cursor = conn.cursor()
sql_querry = """
INSERT INTO test_table (id, name)
VALUES (9, 'Pippo Franco')
"""

cursor.execute(sql_querry)
if input("Do you want to commit? (y/n)") == "y":
    # while the input is pending, a journal file is created.
    conn.commit()

for row in cursor:
    print(row)

conn.close()

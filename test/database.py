import psycopg2

connection = psycopg2.connect(  database    = "ptt_sample",
                                user        = "postgres",
                                host        = "localhost",
                                password    = "p05tgr35ql",
                                port        = 5432)

cursor = connection.cursor()

command = """SELECT * FROM EMPLOYEE"""

cursor.execute(command)

# print(cursor.fetchall())
for item in cursor.fetchall():
    print(item)

connection.close()
import psycopg2
class SQLserver():
    def __init__(self):
        self.connection = psycopg2.connect(database="ptt_sample",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)

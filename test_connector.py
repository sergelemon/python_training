from task16_0 import MySqlConnector

sql0 = "DROP DATABASE IF EXISTS {db};"
sql1 = "CREATE DATABASE {db} CHARACTER  SET utf8 COLLATE utf8_unicode_ci;"
sql2 = """
    CREATE TABLE {db}.{table}  (
    id integer primary key,
    description varchar(255)
    );
    """

db_name = 'mydb'
table_name = 'test_table'

conn = MySqlConnector('test_connection')
conn.open()
print(conn)

conn.create(sql1.format(db=db_name))
res = conn.select('SHOW DATABASE')
print(res)

conn.close()
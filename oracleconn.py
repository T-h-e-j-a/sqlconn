import cx_Oracle
conn=cx_Oracle.Connection(user='scott',password='tiger')
print(conn)



def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into theju(id,name) values(:id,:name)",record)
    conn.commit()
insertrecord(3,'theja')
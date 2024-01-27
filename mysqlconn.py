import pymysql
connect=pymysql.Connection(user='root',password='root',host='localhost',port=3306,db='conn')
# print(connect)
cur=connect.cursor()

def createtable():
    query='''create table theju(
        id int(2) primary key,
        name varchar(50)                     
    );
    '''
    cur.execute(query)                          #execute query only one time otherwise it give table already exist         
# createtable()
def insertrecord(sid,name):
    record=[sid,name]
    cur.execute("insert into theju(id,name) values(%s,%s)",record)
    
    connect.commit()
# insertrecord(2,'chandu')
# insertrecord(3,'chuchu')
# insertrecord(4,'theja')




def read_record():
    query='select * from theju'
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
# read_record()




def fetch_record(sid):
    query='select * from theju where id=%s'
    cur.execute(query,sid)
    record=cur.fetchall()
    for row in record:
        print(row)
# fetch_record(2)


def update_name(sid):
    fetch_record(sid)
    name=input('enter new name to update:-')
    record=[name,sid]
    query='update theju set name=%s where id=%s'
    cur.execute(query,record)
    connect.commit()
    fetch_record(sid)
# update_name(2)

def delete_name(sid):
    # fetch_record(sid)
    # record=[sid]
    query='delete from theju where id=%s'
    cur.execute(query,record)
    connect.commit()
    # fetch_record(sid)
# delete_name(2)




import csv

def read_recors():
    query='select * from theju'
    cur.execute(query)
    records=cur.fetchall()
    # for rows in records:
    #     print(row)
    # with open('new.csv','w',newline='') as csvfile:
    #     data=csv.writer(csvfile)
    #     data.writerow(['id','name'])
    #     for row in records:
    #         data.writerow(row)
# read_recors()



def insert_from_csv():
    with open('new.csv','r',newline='') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])             #insertrecord is the function name given above to insert records
insert_from_csv()



def truncate():
    query='truncate table theju'
    cur.execute(query)
# truncate()




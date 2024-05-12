import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="itsomkar30",
    database="bank"

)

cursor = mydb.cursor()


def createusertable():
    cursor.execute('''
        create table if not exists customers(
        username varchar(20),
        password varchar(20),
        name varchar(20),
        age integer,
        city varchar(20),
        account_number integer,
        status boolean)
    ''')


mydb.commit()

if __name__=="__main__":
    createusertable()


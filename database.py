#Database Management Banking
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root", #your_database_user
    passwd="password", #your_database_password
    database="bank" #database_name
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                credit_name varchar(50) not null,
                credit_bal integer not null,
                status BOOLEAN NOT NULL)
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()

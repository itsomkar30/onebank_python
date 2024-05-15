#Bank Services
from database import *

from relatedvar import *
from tkinter import messagebox
import datetime

# global user2
# user2 = user1
userglobal=user1

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")

    def balanceequiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        # print(f"{self.__username} Balance is {temp[0][0]}")
        # balance =str(temp[0][0])
        # return temp[0][0]
        return temp[0][0]

    def deposit(self, amount):
        print(self.__account_number)
        # print(user1)
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(temp)
        test = amount + temp[0][0]
        print(test)
        db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
        self.balanceequiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")

        # print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")
        messagebox.showinfo("Amount Deposit", f"Amount deposited to your A/C {self.__account_number}")

    def withdraw(self, amount):
        # temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(userglobal)
        # temp2 = db_query(f"SELECT balance FROM customers WHERE username = '{userglobal}';")
        temp2=self.balanceequiry()
        print("balance is",temp2)
        # balance1=self.balanceequiry()

        # if amount > temp2[0][0]:
        if amount > temp2:
            # print("Insufficient Balance Please Deposit Money")
            messagebox.showinfo("Insufficient Balance", f"Insufficient balance in your A/C {returnacc()}")
        else:
            # test = temp2[0][0] - amount
            test = temp2 - amount
            # test = balance1 - amount
            db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
            self.balanceequiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{returnacc()}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            # print(f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")
            messagebox.showinfo("Amount Withdraw", f"Amount withdrawn to your A/C {returnacc()}")

    def fundtransfer(self, receive, amount):
        # temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        temp=self.balanceequiry()
        # if amount > temp[0][0]:
        if amount > temp:
            # print("Insufficient Balance Please Deposit Money")
            messagebox.showinfo("Insufficient Balance", f"Insufficient balance in your A/C {self.__account_number}")
        else:
            temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = '{receive}';")
            # test1 = temp[0][0] - amount
            # test2 = amount + temp2[0][0]
            test1 = temp - amount
            test2 = amount + temp2[0][0]
            db_query(f"UPDATE customers SET balance = '{test1}' WHERE username = '{self.__username}'; ")
            db_query(f"UPDATE customers SET balance = '{test2}' WHERE account_number = '{receive}'; ")
            receiver_username  = db_query(f"SELECT username FROM customers where account_number = '{receive}';")
            self.balanceequiry()
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{returnacc()}',"
                     f"'Fund Transfer From {returnacc()}',"
                     f"'{amount}'"
                     f")")
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{returnacc()}',"
                     f"'Fund Transfer -> {receive}',"
                     f"'{amount}'"
                     f")")
            # print(f"{self.__username} Amount is Sucessfully Transaction from Your Account {self.__account_number}")
            messagebox.showinfo("Transaction Successful", f"Amount is Sucessfully Transaction from Your A/C {returnacc()}")




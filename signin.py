from customtkinter import *
from PIL import Image
from register import *
from customer import *
from bank import *
from database import *
import tkinter as tk
from showhistory import *
from tkinter import messagebox
from tkinter import simpledialog
import random


def sign_in():
    username = user_entry.get()
    password = pass_entry.get()
    success = CTkLabel(master=input1, text="", width=200, corner_radius=3)
    success.grid(row=3, columnspan="2", sticky="nw", pady=(30, 0), padx=(30, 0))
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:

            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            if temp[0][0] == password:
                success.configure(text="Sign in Successful")
                # root.destroy()
                return username
            else:
                success.configure(text="Sign in Failed")
                # sign_in()
    else:
        success.configure(text="User not found")
        return None


def load():
    global userfinal
    userfinal = sign_in()
    root.destroy()
    global account_number

    banking_home()


def get_account_number1():
    query = f"SELECT account_number FROM customers WHERE username = '{userfinal}';"
    result = db_query(query)
    if result:
        return result[0][0]  # Return the account number if found
    else:
        return None


def banking_home():
    def __init__(self, username, account_number):
        # account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{userfinal}';")

        self.username = username
        self.account_number = account_number
        # self.account_number = account_number

    root = CTk()
    root.geometry("600x480")
    root.resizable(0, 0)
    root.title("Home Onebank")
    nunito = ("Nunito ExtraBold")
    nunitosemi = ("Nunito SemiBold")

    img = Image.open("assets/banking.png")
    logo = Image.open("assets/bank-logo.png")
    email_icon_data = Image.open("assets/user.png")
    password_icon_data = Image.open("assets/lock.png")

    account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
    global user1
    user1 = userfinal
    # account_number = 25260346
    # user = "omkar"
    root1 = CTkFrame(master=root, height=600, width=480)

    def get_account_number():
        query = f"SELECT account_number FROM customers WHERE username = '{user1}';"
        result = db_query(query)
        if result:
            return result[0][0]  # Return the account number if found
        else:
            return result[0][0]  # Return None if no account number found for the username

    global acc_bal_new
    acc_bal_new = get_account_number()

    def bal_enq():
        bobj = Bank(user1, account_number)
        bal = bobj.balanceequiry()

        messagebox.showinfo("Balance Enquiry", f"Avaliable Balance is '{bal}'")

    def cash_deposit():
        print(userfinal)
        # account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{userfinal}';")
        account_number = get_account_number()

        dep_amount = simpledialog.askinteger("Deposit", "Enter amount to Deposit :")

        # bobj = Bank(user, account_number[0][0])
        bobj = Bank(user1, account_number)
        bobj.deposit(dep_amount)
        mydb.commit()
        # cash_deposit(amount)

    def cash_withdraw():
        with_amount = simpledialog.askinteger("Withdraw", "Enter amount to Withdraw :")
        # bobj = Bank(user, account_number[0][0])
        bobj = Bank(user1, account_number)
        bobj.withdraw(with_amount)
        mydb.commit()

    def fund_transfer():
        receiver = simpledialog.askinteger("Fund Transfer", "Enter Receiver's A/C Number :")
        amount = simpledialog.askinteger("Fund Transfer", f"Enter amount to Transfer to {receiver} :")
        # bobj = Bank(user, account_number[0][0])
        bobj = Bank(user1, account_number)
        bobj.fundtransfer(receiver, amount)
        mydb.commit()

    def userhistory():
        # history.showhistory(user1)
        history(user1)

    frame = CTkFrame(master=root, width=600, height=480, fg_color="#ffffff", corner_radius=0)
    frame.pack_propagate(0)
    # frame.pack(expand=True,side="right")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    CTkLabel(master=frame, text="Welcome!", text_color="#601E88", anchor="w", justify="left", font=(nunito, 30)).pack(
        anchor="w", pady=(40, 0), padx=(50, 0))
    CTkLabel(master=frame, text="Services", text_color="#7E7E7E", anchor="w", justify="center",
             font=(nunitosemi, 18)).pack(anchor="w", padx=(50, 0))
    # CTkLabel(master=frame,text="  User : ",text_color="#601E88",anchor="w",justify="left",font=("Arial Bold",15),image=user,compound="left").pack(anchor="w",pady=(38,0),padx=(25,0))
    ###

    input1 = CTkFrame(master=frame, fg_color="#ffffff")
    input1.pack_propagate(0)
    input1.pack(expand=True, pady=(25, 0), padx=(20, 0), anchor="nw")
    # input1.place(relx=0.5, rely=0.5, anchor="center")

    balance_enq = CTkButton(master=input1, text="Balance Enquiry", hover_color="#601E88", command=bal_enq, width=200,
                            corner_radius=3).grid(row=0, columnspan="2", sticky="nw", pady=(20, 0), padx=(30, 0))
    cash_dep = CTkButton(master=input1, text="Cash Deposit", hover_color="#601E88", command=cash_deposit, width=200,
                         corner_radius=3).grid(row=1, columnspan="2", sticky="nw", pady=(20, 0), padx=(30, 0))
    cash_with = CTkButton(master=input1, text="Cash Withdraw", hover_color="#601E88", command=cash_withdraw, width=200,
                          corner_radius=3).grid(row=2, columnspan="2", sticky="nw", pady=(20, 0), padx=(30, 0))
    fund_trans = CTkButton(master=input1, text="Fund Transfer", hover_color="#601E88", command=fund_transfer, width=200,
                           corner_radius=3).grid(row=3, columnspan="2", sticky="nw", pady=(20, 0), padx=(30, 0))
    fund_trans = CTkButton(master=input1, text="Transaction History", hover_color="#601E88", command=userhistory,
                           width=200, corner_radius=3).grid(row=4, columnspan="2", sticky="nw", pady=(20, 0),
                                                            padx=(30, 0))
    showbal = CTkLabel(master=input1, text=f"Your A/C no is {get_account_number()}", text_color="red", width=200).grid(
        row=5, columnspan="2", sticky="nw", pady=(20, 0), padx=(30, 0))

    acc_bal_new = get_account_number()

    root.mainloop()


root = CTk()
root.geometry("600x480")
root.resizable(0, 0)
root.title("Sign-in Onebank")
nunito = ("Nunito ExtraBold")
nunitosemi = ("Nunito SemiBold")

img = Image.open("assets/banking.png")
logo = Image.open("assets/bank-logo.png")
email_icon_data = Image.open("assets/user.png")
password_icon_data = Image.open("assets/lock.png")

image = CTkImage(light_image=img, dark_image=img, size=(300, 400))
logo = CTkImage(light_image=logo, dark_image=logo, size=(300, 80))
user = CTkImage(light_image=email_icon_data, size=(19, 19))
password1 = CTkImage(light_image=password_icon_data, size=(20, 20))

Lside = CTkLabel(master=root, text="", image=image).pack(expand=True, side="left")

frame = CTkFrame(master=root, width=300, height=480, fg_color="#ffffff", corner_radius=0)
frame.pack_propagate(0)
frame.pack(expand=True, side="right")
CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=(nunito, 30)).pack(
    anchor="w", pady=(50, 0), padx=(40, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
         font=(nunitosemi, 18)).pack(anchor="w", padx=(50, 0))
# CTkLabel(master=frame,text="  User : ",text_color="#601E88",anchor="w",justify="left",font=("Arial Bold",15),image=user,compound="left").pack(anchor="w",pady=(38,0),padx=(25,0))
###
input1 = CTkFrame(master=frame, fg_color="#ffffff")
input1.pack_propagate(0)
input1.pack(expand=True, pady=(38, 0), padx=(20, 0), anchor="nw")
CTkLabel(master=input1, text="", image=user, justify="left").grid(row=0, column=0, sticky="nw", pady=(5, 0))
user_entry = (
    CTkEntry(master=input1, placeholder_text="Username", fg_color="transparent", text_color="black", corner_radius=2,
             width=200))
user_entry.grid(row=0, column=1, sticky="nw", padx=(10, 0), pady=(5, 0))

CTkLabel(master=input1, text="", image=password1, justify="left").grid(row=1, column=0, sticky="nw", pady=(20, 0))
pass_entry = (
    CTkEntry(master=input1, placeholder_text="Password ", fg_color="transparent", show="*", text_color="black",
             corner_radius=2, width=200))
pass_entry.grid(row=1, column=1, sticky="nw", padx=(10, 0), pady=(20, 0))

button = CTkButton(master=input1, text="Submit", hover_color="#601E88", command=load, width=200, corner_radius=3).grid(
    row=2, columnspan="2", sticky="nw", pady=(30, 0), padx=(30, 0))
# success = CTkLabel(master=input1,text="",width=200,corner_radius=3).grid(row=3,columnspan="2",sticky="nw",pady=(30,0),padx=(30,0))


root.mainloop()

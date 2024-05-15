from customtkinter import *
from PIL import Image
from bank1 import Bank
from customer import *
import random

import time



root = CTk()
root.geometry("600x480")
root.resizable(0,0)
root.title("Sign-in Onebank")
nunito=("Nunito ExtraBold")
nunitosemi=("Nunito SemiBold")

img = Image.open("assets/banking.png")
logo = Image.open("assets/bank-logo.png")
email_icon_data = Image.open("assets/user.png")
password_icon_data = Image.open("assets/lock.png")


frame = CTkFrame(master=root,width=300,height=480,fg_color="#ffffff",corner_radius=0)
frame.pack_propagate(0)
frame.pack(expand=True,side="right")
CTkLabel(master=frame,text="Welcome!",text_color="#601E88",anchor="w",justify="left",font=(nunito,30)).pack(anchor="w",pady=(40,0),padx=(50,0))
CTkLabel(master=frame, text="Sign up to your account", text_color="#7E7E7E", anchor="w", justify="left", font=(nunitosemi, 18)).pack(anchor="w", padx=(50, 0))

input1 = CTkFrame(master=frame,fg_color="#ffffff")
input1.pack_propagate(0)
input1.pack(expand=True,pady=(25,0),padx=(20,0),anchor="nw")



ac = CTkLabel(master=input1,text=f"",text_color="red",width=200)
ac.grid(row=6,columnspan="2",sticky="nw",pady=(20,0),padx=(30,0))




def acc_no():
    while True:
        account_number = int(random.randint(10000000, 99999999))
        temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
        if temp:
            continue
        else:
            time.sleep(1)
            # print("Your Account Number",account_number)
            ac.configure(text=f'Your Account number is {account_number}')
            # credit_name="Platinium Credit Card"
            # credit_bal=100000
            # return account_number
            username= user_entry.get()
            password=pass_entry.get()
            name= name_entry.get()
            age= age_entry.get()
            city= city_entry.get()
            username= user_entry.get()
            credit_name="Platinium Credit Card"
            credit_bal=100000
            cobj = Customer(username, password, name, age, city, account_number,credit_name,credit_bal)
            cobj.createuser()
            bobj = Bank(username, account_number)
            bobj.create_transaction_table()
            time.sleep(3)
            root.destroy()



            break




image = CTkImage(light_image=img,dark_image=img,size=(300,400))
logo = CTkImage(light_image=logo,dark_image=logo,size=(300,80))
user = CTkImage(light_image=email_icon_data,size=(19,19))
password = CTkImage(light_image=password_icon_data,size=(20,20))

Lside = CTkLabel(master=root,text="",image=image).pack(expand=True,side="left")

# frame = CTkFrame(master=root,width=300,height=480,fg_color="#ffffff",corner_radius=0)
# frame.pack_propagate(0)
# frame.pack(expand=True,side="right")
# CTkLabel(master=frame,text="Welcome!",text_color="#601E88",anchor="w",justify="left",font=(nunito,30)).pack(anchor="w",pady=(40,0),padx=(50,0))
# CTkLabel(master=frame, text="Sign up to your account", text_color="#7E7E7E", anchor="w", justify="left", font=(nunitosemi, 18)).pack(anchor="w", padx=(50, 0))

# input1 = CTkFrame(master=frame,fg_color="#ffffff")
# input1.pack_propagate(0)
# input1.pack(expand=True,pady=(25,0),padx=(20,0),anchor="nw")
# CTkLabel(master=input1,text="",image=user,justify="left").grid(row = 0,column = 0,sticky="nw",pady=(5,0))
user_entry = (CTkEntry(master=input1,placeholder_text="Create Username",fg_color="transparent",text_color="black",corner_radius=2,width=200))
user_entry.grid(row = 0, column= 1,sticky = "nw",padx=(30,0),pady=(0,0))
# CTkLabel(master=input1,text="",image=password,justify="left").grid(row = 1,column = 0,sticky="nw",pady=(20,0))
pass_entry = (CTkEntry(master=input1,placeholder_text="Password ",fg_color="transparent",show="*",text_color="black",corner_radius=2,width=200))
pass_entry.grid(row = 1, column= 1,sticky = "nw",padx=(30,0),pady=(20,0))

name_entry = (CTkEntry(master=input1,placeholder_text="Name",fg_color="transparent",text_color="black",corner_radius=2,width=200))
name_entry.grid(row = 2, column= 1,sticky = "nw",padx=(30,0),pady=(20,0))

age_entry = (CTkEntry(master=input1,placeholder_text="Age",fg_color="transparent",text_color="black",corner_radius=2,width=200))
age_entry.grid(row = 3, column= 1,sticky = "nw",padx=(30,0),pady=(20,0))

city_entry = (CTkEntry(master=input1,placeholder_text="City",fg_color="transparent",text_color="black",corner_radius=2,width=200))
city_entry.grid(row = 4, column= 1,sticky = "nw",padx=(30,0),pady=(20,0))


button = CTkButton(master=input1,text="Submit",hover_color="#601E88",command=acc_no,width=200,corner_radius=3).grid(row=5,columnspan="2",sticky="nw",pady=(20,0),padx=(30,0))


root.mainloop()
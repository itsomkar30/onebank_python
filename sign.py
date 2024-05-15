from customtkinter import *
from PIL import Image


app = CTk()
app.geometry("600x480")
app.resizable(0,0)
app.title("Onebank")
nunito=("Nunito ExtraBold")
nunitosemi=("Nunito SemiBold")

side_img_data = Image.open("assets/side-img.png")
bank_logo_light = Image.open("assets/bank-logo.png")
bank_logo_dark = Image.open("assets/logo_dark.png")
# email_icon_data = Image.open("email-icon.png")
# password_icon_data = Image.open("password-icon.png")
# google_icon_data = Image.open("google-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
bank_logo = CTkImage(dark_image=bank_logo_dark, light_image=bank_logo_dark,size=(300, 70))
# email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
# password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
# google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")
CTkLabel(master=frame, text="", image=bank_logo).pack(expand=False, side="top",pady=(40,0))

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=(nunito, 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=( nunito, 13)).pack(anchor="w", padx=(25, 0))



button = CTkButton(master=frame,text="Sign in",hover_color="#601E88",command="",width=250,corner_radius=3,font=(nunitosemi,13)).pack(anchor="w", padx=(25, 0), pady=(10,10))
button = CTkButton(master=frame,text="Sign up",hover_color="#601E88",command="",width=250,corner_radius=3,font=(nunitosemi,13)).pack(anchor="w",  padx=(25, 0), pady=(10,10) )


app.mainloop()
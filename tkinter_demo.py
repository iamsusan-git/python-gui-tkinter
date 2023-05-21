from tkinter import *
from PIL import ImageTk, Image   # libary to dispay image
from tkinter import messagebox


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'susanp977@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy', 'login sucessful')

    else:
        messagebox.showerror('Error', 'Login Failed')    



root = Tk()

root.title('Login Form')          # title change
root.iconbitmap('favicon.ico')    #logo change

root.geometry('350x500')       #parcticular window

root.configure(background='navy')    #Back ground color
img = Image.open('flipkart-logo.png')

resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady =(10,10))


text_lable = Label(root,text ='Flipkart',fg ='white', bg='#0096DC')
text_lable.pack()
text_lable.config(font=('verdana',24))

email_label = Label(root,text='Enter Email',fg ='white', bg='Orange')
email_label.pack(pady =(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


password_label = Label(root,text='Enter Password',fg='white',bg='Orange')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root, text ='Login Here', bg='white', fg= 'black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields can not be empty')
    elif usernameEntry.get()=='Nitin' and passwordEntry.get()=='2505':
        messagebox.showinfo('Success','Welcome')
        root.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter the correct details')
        


root = Tk()
root.title('Login System Of Student Management System')
root.geometry('1250x750')
root.resizable(False, False)

BackGroundImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(root, image=BackGroundImage)
bgLabel.place(x=0, y=0)


loginFrame=Frame(root,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')


logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10,padx=20)

usernameImage=PhotoImage(file='user.png')
usernamelabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman ',20,'bold'),bg='white')
usernamelabel.grid(row=1,column=0,pady=10)

usernameEntry=Entry(loginFrame,font=('times new roman ',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage=PhotoImage(file='password.png')
passwordlabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman ',20,'bold'),bg='white')
passwordlabel.grid(row=2,column=0,pady=10)

passwordEntry=Entry(loginFrame,font=('times new roman ',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman ',14,'bold'),width=15,fg='white'
                   ,bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white'
                   ,cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

loginButton=Label(loginFrame,text='Projected By Nitin',font=('times new roman ',22,'bold'),width=15,fg='black'
                   ,bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white'
                   ,cursor='hand2')
loginButton.grid(row=8,column=3,pady=10)

root.mainloop()

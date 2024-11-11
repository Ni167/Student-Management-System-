from tkinter import *
import time
import ttkthemes
import pymysql
from tkinter import ttk,messagebox,filedialog
import pandas


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        window.destroy()
    else:
        pass


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added_Date','Added_time'])
    try:
        table.to_csv(url,index=False)
        messagebox.showinfo('Success','Data is saved successfully')
    except:
        pass
        



def toplevel_data(title,button_text,command):    
    global idEntry,nameEntry,phoneEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)

    
    idLabel=Label(screen,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    phoneLabel=Label(screen,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(screen,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel=Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)


    screen_student_button=ttk.Button(screen,text=button_text,command=command)
    screen_student_button.grid(row=7,columnspan=2,pady=15)

    if title=='Update Student':
        indexing=studentTable.focus()
        
        content=studentTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        phoneEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])
    



def update_data():
    try:
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                    genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is updated successfully',parent=screen)
        screen.destroy()
        show_student()
    except:
        pass
        


        
    



def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

    
    

def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def search_data():
    query='select * from student where id=%s or name=%s or mobile=%s  or email=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)
    
    






def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or  phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Fields are required',parent=screen)
        
    else:
        pass
            
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                        genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                screen.destroy()

        except:
            messagebox.showerror('Error','Id can not be repeated',parent=screen)
            return

        query='select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)
            
    



def connect_database():
    def connect():
        global mycursor,con
        try:            
            con = pymysql.connect(
                host='localhost',
                user='root',
                password='pooja2504'
            )
            mycursor = con.cursor()
                        
        except:
            messagebox.showerror('Error','Invalid Details', parent=connectWindow)
            return
        
        try:    
         
            mycursor.execute('CREATE DATABASE IF NOT EXISTS studentmanagementsystem')
            mycursor.execute('USE studentmanagementsystem')
        
        
            mycursor.execute('''
                CREATE TABLE IF NOT EXISTS student (
                    id INT PRIMARY KEY,
                    name VARCHAR(30),
                    mobile VARCHAR(10),
                    email VARCHAR(30),
                    address VARCHAR(100),
                    gender VARCHAR(20),
                    dob VARCHAR(20),
                    date VARCHAR(50),
                    time VARCHAR(50)
                )
            ''')
            messagebox.showinfo('Success', 'Database and table created successfully', parent=connectWindow)
        except:
            mycursor.execute('use studentmanagementsystem')
            messagebox.showinfo('Success', 'Database connection is successful', parent=connectWindow)

        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)

        

            
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)


    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)


    
    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)


    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)


    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=5,columnspan=2)


    

count=0
text=''
def slider():
    global text,count
    if count==len(s):        
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count=count+1
    sliderLabel.after(300,slider)


zero=0
name=''
def owner():
    global name,zero
    if zero==len(j):        
        zero=0
        name=''
    name=name+j[zero]
    owner_name.config(text=name)
    zero=zero+1
    owner_name.after(420,owner)







def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)    




window=ttkthemes.ThemedTk()
window.get_themes()


window.set_theme('radiance')


window.geometry('1200x700+0+0')
window.resizable(0,0)
window.title('Student Management System')



datetimeLabel=Label(window,font=('times new romsn',17,'bold'))
datetimeLabel.place(x=5,y=5)
clock()


s='Student Management System'
sliderLabel=Label(window,text=s,font=('arial',30,'bold'),width=30)
sliderLabel.place(x=270,y=9)

slider()

j='Projected By Nitin'
owner_name=Label(window,text=j,font=('arial',15,'bold'),width=30)
owner_name.place(x=887,y=50)

owner()



connectButton=ttk.Button(window,text='Connect to Database',command=connect_database)
connectButton.place(x=980,y=10)

leftFrame=Frame(window)
leftFrame.place(x=50,y=80,width=300,height=600)


logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda:toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)


searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda:toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)


updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda:toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)


showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)


exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)


rightFrame=Frame(window)
rightFrame.place(x=350,y=80,width=820,height=600)


scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)


scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)


studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=180,anchor=CENTER)
studentTable.column('Added Time',width=180,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=30,font=('arail',12,'bold'),foreground='black',background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='black')


 



studentTable.config(show='headings')

window.mainloop()

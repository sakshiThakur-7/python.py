from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    userNameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    confirm_PasswordEntry.delete(0,END)
    check.set(0)

def login_page():
    signUp_window.destroy()
    import LoginPage

def connect_database():
    if emailEntry.get()=='' or userNameEntry.get()=='' or PasswordEntry.get()==''or confirm_PasswordEntry.get()=='':
        messagebox.showerror('Error','All Field Are Required')
    elif PasswordEntry.get() != confirm_PasswordEntry.get():
        messagebox.showerror('Error','Password Missmatch !!')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept terms and conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='sakshi@123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Pleases Try Again !!')
            return
        try:
            query='create database user_data'
            mycursor.execute(query)
            query='use user_data'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use user_data')

        query='select * from data where username=%s'
        mycursor.execute(query,(userNameEntry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','User name already exist !!')
        else:
            query='insert into data(email,username,password)values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),userNameEntry.get(),PasswordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration Is Successful')
            clear()

        signUp_window.destroy()
        import LoginPage



#------------------------------------------------->   WINDOW    <------------------------------------------------------
signUp_window = Tk()
signUp_window.title("Sign Up Page")
signUp_window.configure(bg='white')
signUp_window.iconbitmap("TKINTER/TKINTER LIBRARY/check-form_116472.ico")
signUp_window.geometry('900x600')
# #-----------|  window is now in fix size  |-------
signUp_window.resizable(0,0)
#-----------|  add background Image in window   |--------
bgImage = ImageTk.PhotoImage(file='TKINTER/TKINTER LIBRARY/plash (2).png')
bgLabel= Label(signUp_window,image=bgImage,bd=0)
bgLabel.grid()
bgLabel.place(x=00,y=100)

frame=Frame(signUp_window,width=250,height=10,bg='white',bd=0)
frame.place(x=475,y=150)


# ------------------------------------------------------->|(inside the Frame)|<------------------------------------------------------
#-------------------------------------------->   HEADING   <-----------------------------------------------------
heading=Label(frame,text="Create An Account",font=('Open Sans',20,"bold"),fg="DeepSkyBlue4",bg="white",bd=10,relief=FLAT)
heading.grid(row=0,column=0,padx=0,pady=0)


#-------------------------------------------->  Email  <-----------------------------------------------------
email=Label(frame,text="Email",font=('open look cursor',12,'bold'),bg="white",fg="midnight blue")
email.grid(row=1,column=0,sticky='w',padx=40,pady=(5,0))

emailEntry=Entry(frame,width=30,font=('Open Sans',11),bg="sky blue",fg="black")
emailEntry.grid(row=2,column=0,sticky='w',padx=40)


#-------------------------------------------->  User Name  <-----------------------------------------------------
userName=Label(frame,text="User Name",font=('open look cursor',11,'bold'),bg="white",fg="midnight blue")
userName.grid(row=3,column=0,sticky='w',padx=40,pady=(5,0))

userNameEntry=Entry(frame,width=30,font=('Open Sans',11),bg="sky blue",fg="black")
userNameEntry.grid(row=4,column=0,sticky='w',padx=40)


#-------------------------------------------->  Password  <-----------------------------------------------------
Password=Label(frame,text="Password",font=('open look cursor',11,'bold'),bg="white",fg="midnight blue")
Password.grid(row=5,column=0,sticky='w',padx=40,pady=(5,0))

PasswordEntry=Entry(frame,width=30,font=('Open Sans',11),bg="sky blue",fg="black")
PasswordEntry.grid(row=6,column=0,sticky='w',padx=40)


#-------------------------------------------->  Confirm Password  <-----------------------------------------------------
confirm_Password=Label(frame,text="Confirm Password",font=('open look cursor',12,'bold'),bg="white",fg="midnight blue")
confirm_Password.grid(row=7,column=0,sticky='w',padx=40,pady=(5,0))

confirm_PasswordEntry=Entry(frame,width=30,font=('Open Sans',11),bg="sky blue",fg="black")
confirm_PasswordEntry.grid(row=8,column=0,sticky='w',padx=40)


#-------------------------------------------->  term condition checkbox  <-----------------------------------------------------
check=IntVar()
agree=Checkbutton(frame,text="I agree to the Term & conditions",font=('open look cursor',9,"bold"),bg="white",fg="black",
                  activebackground="white",activeforeground="red",cursor='hand2',variable=check)
agree.grid(row=9,column=0,sticky='w',padx=40,pady=10)


#-------------------------------------------->  SignUp button  <-----------------------------------------------------
SignUp=Button(frame,text="Sign Up",font=('Open Sans',15,'bold'),width=20,bg="orange",fg="white",
             activeforeground='white',activebackground='Pink',cursor='hand2',bd=0,command=connect_database)
SignUp.grid(row=10,column=0,sticky='w',padx=40,pady=(5,0))


#-------->   no account LABEL   <----------
noAcc =Label(frame,text="Don't have an account? ",font=('Open Sans',10,'bold'),fg='midnight blue',bg='white')
noAcc.grid(row=11,column=0,sticky='w',padx=40,pady=(5,0))


#-------->   Login Button   <----------
login=Button(frame,text="log in",font=('Open Sans',11,' bold underline'),bg="white",fg="red",
             activeforeground='white',activebackground='grey20',cursor='hand2',bd=0,command=login_page)
login.place(x=205,y=346)

signUp_window.mainloop()
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk 
import pymysql
#------|  Functions  |-------
def forget():
    def change_password():
        if reset_user_Entry.get()=='' or reset_new_Entry.get()=='' or reset_confirm_Entry.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=reset_window)
        elif reset_new_Entry.get() != reset_confirm_Entry.get():
            messagebox.showerror('Error','Passord and confirm password are not same',parent=reset_window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='sakshi@123',database='user_data')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(reset_user_Entry.get()))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"incorrect username",parent=reset_window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(reset_new_Entry.get(),reset_user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success',"password is reset,please login with new password",parent=reset_window)
                reset_window.destroy()

    #-----------------------------------------------------------------------------------------------------------------------------------------#
    #                                                       RESET PASSWORD WINDOW                                                             #
    # ----------------------------------------------------------------------------------------------------------------------------------------#
    reset_window = Toplevel()
    reset_window.title("Reset Password Page")
    reset_window.configure(bg='white')
    reset_window.iconbitmap("TKINTER/TKINTER LIBRARY/check-form_116472.ico")
    reset_window.geometry('900x550')
    reset_window.resizable(0,0)
   
    bgImage = ImageTk.PhotoImage(file='TKINTER/TKINTER LIBRARY/plash (1).png')
    bgLabel= Label(reset_window,image=bgImage,bd=0)
    bgLabel.grid()
   
    # -------------------------------------         HEADING         --------------------------------------------------
    reset_heading=Label(reset_window,text="RESET PASSWORD",font=('arial',20,'bold'),bg='white',fg='goldenrod')
    reset_heading.place(x=520,y=80)

    # -------------------------------------         USER NAME         -------------------------------------------------- 
    reset_user =Label(reset_window,text="Username",font=('arial',16),bg='white',fg='SpringGreen4') 
    reset_user.place(x=520,y=140)

    reset_user_Entry = Entry(reset_window,width=30,font=('arial',10),bd=0)
    reset_user_Entry.place(x=520,y=170)
   
    frame12= Frame(reset_window,width=280,height=1,bg="dark olive green")
    frame12.place(x=520,y=190)

    # -------------------------------------         NEW Password         -------------------------------------------------- 
    reset_new =Label(reset_window,text="New Password",font=('arial',16),bg='white',fg='SpringGreen4') 
    reset_new.place(x=520,y=200)

    reset_new_Entry = Entry(reset_window,width=30,font=('arial',10),bd=0)
    reset_new_Entry.place(x=520,y=230)

    frame13= Frame(reset_window,width=280,height=1,bg="dark olive green")
    frame13.place(x=520,y=250)

    # -------------------------------------         CONFIRM Password         -------------------------------------------------- 
    reset_confirm =Label(reset_window,text="Confirm Password",font=('arial',16),bg='white',fg='SpringGreen4') 
    reset_confirm.place(x=520,y=260)

    reset_confirm_Entry = Entry(reset_window,width=30,font=('arial',10),bd=0)
    reset_confirm_Entry.place(x=520,y=290)

    frame14= Frame(reset_window,width=280,height=1,bg="dark olive green")
    frame14.place(x=520,y=310)

    # ----------------------------------               SUBMIT        -------------------------------------------------------------------
    submit=Button(reset_window,text="Submit",font=('Microsoft Yahei UI Light',15,'bold'),width=23,bg="steel blue",fg="white",
                activeforeground='white',activebackground='sky blue',cursor='hand2',bd=0,command=change_password)
    submit.place(x=520,y=350)


    reset_window.mainloop()




def login_user():
    if userName.get()=='' or Password.get()=='':
        messagebox.showerror('Error','All Fields Are Require')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='sakshi@123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Pleases Try Again !!')
            return
        
        query='use user_data'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(userName.get(),Password.get()))
        row=mycursor.fetchone()
        if row== None:
            messagebox.showerror('Error','Invalid usernme or password')
        else:
            messagebox.showinfo('Welcome','login successfull')


def hide():
    #change open eye to close eye when click
    openEye.config(file='TKINTER/TKINTER LIBRARY/eye_close_icon_178650.png')
    #show star in password
    Password.config(show='*')

    eyeButton.config(command=show)

def show():
    openEye.config(file='TKINTER/TKINTER LIBRARY/eye_icon-icons.com_50398.png')
    Password.config(show='')
    eyeButton.config(command=hide)

def user_entery(event):
    if userName.get()=='User Name ':
        userName.delete(0,END)
def password_entry(event):
    if Password.get()=='Password':
        Password.delete(0,END)

def signup_Page():
    window.destroy()
    import signUpPage


#!!!!----!!!!!!!!!!!----------------!!! GUI  !!!!----!!!!!!!!!!!----------------!!!

#------------------------------------------------->   WINDOW    <------------------------------------------------------
window = Tk()
window.title("Registration Form")
window.configure(bg='white')
window.iconbitmap("TKINTER/TKINTER LIBRARY/check-form_116472.ico")
window.geometry('900x700')
# #-----------|  window is now in fix size  |-------
window.resizable(0,0)
#-----------|  add background Image in window   |--------
bgImage = ImageTk.PhotoImage(file='TKINTER/TKINTER LIBRARY/plash (3).png')
bgLabel= Label(window,image=bgImage,bd=0)
bgLabel.place(x=50,y=100)


#-------------------------------------------->   HEADING    <-----------------------------------------------------
heading=Label(window,text="USER LOGIN",font=('Open Sans',25,'bold'),fg="DarkOrange2",bg="white",bd=12,relief=FLAT)
heading.place(x=520,y=155)

#-------------------------------------------->   USER ENTRY  <----------------------------------------------------
userName=Entry(window,width=25,bg="white",font=('open look cursor',12),fg="navy blue",bd=0)
userName.place(x=520,y=235)
userName.insert(0,"User Name ")

userName.bind('<FocusIn>',user_entery)

frame1= Frame(window,width=230,height=1,bg="midnight blue")
frame1.place(x=520,y=258)

#------------------------------------------>   PASSWORD ENTRY    <-------------------------------------------
Password=Entry(window,width=25,bg="white",font=('open look cursor',12),fg="navy blue",bd=0)
Password.place(x=520,y=276)
Password.insert(0,"Password")

Password.bind('<FocusIn>',password_entry)

frame2= Frame(window,width=230,height=1,bg="midnight blue")
frame2.place(x=520,y=300)

#--------|   EYE BUTTON (open and close eye) |----------
openEye=PhotoImage(file='TKINTER/TKINTER LIBRARY/eye_icon-icons.com_50398.png')
eyeButton=Button(window,image=openEye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=730,y=264)

# #--------|   REMEMBER ME CHECK BUTTON  |----------
# remember_me=Checkbutton(window,text="Remember Me ",width=10,height=1,bg="white",fg='tomato4')
# remember_me.place(x=520,y=330)
 
#--------|   FORGET BUTTON  |----------
forgetButton=Button(window,text="Forgot Password ?",bd=0,bg='white',activebackground='white',
                    cursor='hand2',fg="violet red",font=('Microsoft Yahei UI Light',10,'bold'),command=forget)
forgetButton.place(x=640,y=326)

#--------|   LOGIN BUTTON  |----------
login=Button(window,text="Login",font=('Microsoft Yahei UI Light',15,'bold'),width=20,bg="plum4",fg="white",
             activeforeground='white',activebackground='plum1',cursor='hand2',bd=0,command=login_user)
login.place(x=525,y=365)

#--------|   OR LABEL  |----------
orLabel =Label(window,text='----------------- OR ------------------',font=('Open Sans',14),fg='DeepPink3',bg='white')
orLabel.place(x=520,y=417)

#--------|   Images LABEL (fb,twitter,insta ) |----------
facebook=PhotoImage(file='TKINTER/TKINTER LIBRARY/1490889652-facebook_82510.png')
fbButton=Button(window,image=facebook,bd=0,bg='white',activebackground='white',cursor='hand2')
fbButton.place(x=540,y=455)

twitter=PhotoImage(file='TKINTER/TKINTER LIBRARY/1491579542-yumminkysocialmedia22_83078.png')
twitterButton=Button(window,image=twitter,bd=0,bg='white',activebackground='white',cursor='hand2')
twitterButton.place(x=620,y=455)

insta=PhotoImage(file='TKINTER/TKINTER LIBRARY/1491580635-yumminkysocialmedia26_83102.png')
instaButton=Button(window,image=insta,bd=0,bg='white',activebackground='white',cursor='hand2')
instaButton.place(x=695,y=455)

#--------|   no account LABEL  |----------
noAcc =Label(window,text="Don't have an account? ",font=('Open Sans',9,'bold'),fg='midnightblue',bg='white')
noAcc.place(x=510,y=498)

#--------|   NEW ACCOUNT BUTTON  |----------
newAcc=Button(window,text="Create new account",font=('Open Sans',9,'bold'),width=18,bg="white",fg='red',
             activeforeground='orange3',activebackground='white',cursor='hand2',bd=0,command=signup_Page)
newAcc.place(x=648,y=498)

frame3= Frame(window,width=120,height=1,bg="red")
frame3.place(x=655,y=520)



window.mainloop()
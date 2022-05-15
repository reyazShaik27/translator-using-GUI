#Translator (Translates the text from any language to English)
#Created by Reyaz, Mallikarjun and Bavish
#Importing the necessary packages
import mysql.connector              #To import mysql.connnector for using database
from googletrans import Translator  #To import translator from googletrans module
import pyttsx3                      #To import pyttsx(text-to-speech conversion library in python) module -> text speaker
from tkinter import *               #To import every thing from tkinter module
from tkinter import messagebox      #To import messagebox from tkinter module
root=Tk()                           #To set a root window
root.geometry("800x450")            #To set the geometery of the root window
root.title("Translator")            #To set a title for the root window
root.configure(bg="#CECCBE")        #To set background color for the root window
root.iconbitmap(r'2.ico')           #To set icon for the root window
#Creating variables:
en=StringVar()
i=IntVar()
#Creating and accesing database:
mydb=mysql.connector.connect(host="localhost",user="root",passwd="******",database="translator")             #To connect program with database
mycursor=mydb.cursor()                                                                                          #For accessing the database
#mycursor.execute("create database Translator")                                                 #To create a new database
#mycursor.execute("create table Words (Enteredtext varchar(500),Translatedtext varchar(500))")  #To create a table in the database with two columns
#mydb.commit()                                                                                   #To end the current statement and permenant the changes
#For Translating the text entered by the user:
def trans():
    global word                        #To make variable word global
    word = en.get()                    #To get the text entered by the user
    try:
        if word == "":                     #If text entered by user is empty then
            e="No word is entered"
            er.delete(0,"end")          #To delete the previous text in the Error box
            er.insert("end",e)          #To insert the value of variable e into Error box
        else:                           #If text entered by user is not empty then
            global speech                           #To make variable speech global
            trans = Translator().translate(word)       #To translate the text entered by the user
            speech = trans.text                     #To get the translated text
            txt.delete(0,"end")                     #To delete the previous value in the output box
            txt.insert("end",speech)                #To insert the translated text into the output box
            er.delete(0,"end")                      #To delete the previous text in the Error box
    except:
        e="Not connected to the internet"
        er.delete(0,"end")                          #To delete the previous text in the Error box
        er.insert("end",e)                          #To insert the value in variable e into the Error box
#For Speaking the translated text
def speak():
    try:
        eng = pyttsx3.init()                    #To set the engine to speak
        sound = eng.getProperty("voices")       #To get the voices
        eng.setProperty("voice", sound[1].id)   #To set the voice to lady voice
        eng.say(speech)                         #To speak the translated text
        eng.runAndWait()                        
        er.delete(0,"end")                      #To delete the previous text in the Error box
    except NameError:                           #If the user donot translated the text
        e="No word is translated"
        er.delete(0,"end")                      #To delete the previous text in the Error box
        er.insert("end",e)                      #To insert the value in variable e into the Error box
#Creating a message box while exiting the window
def ext():
    ans=messagebox.askquestion("Confirm Exit", "Are you sure you want to exit Translator?")         #For creating a message box
    if ans == "yes":
        root.destroy()                          #For destroying the window
    else:
        return
#For changing the background color of the window, labels etc.
def cllk():
    root.config(bg="#CECCBE")
    c1.config(bg="#CECCBE")
    c2.config(bg="#CECCBE")
    c3.config(bg="#CECCBE")
    c4.config(bg="#CECCBE")
    el.config(bg="#CECCBE")
    tl.config(bg="#CECCBE")
    f.config(bg="#4c5f7a")
    cl.config(bg="#4c5f7a",fg="#000000")
    c.config(bg="#4c5f7a")
    text.config(bg="#4c5f7a",fg="#000000")
    btp.config(bg="#FFCCFF",fg="#000000")
    lf.config(bg="#4c5f7a",fg="#001f3f")
    f1.config(bg="#CECCBE",fg="#000000")
    f2.config(bg="#CECCBE",fg="#000000")
    f3.config(bg="#CECCBE",fg="#000000")
    f4.config(bg="#CECCBE",fg="#000000")
    f5.config(bg="#CECCBE",fg="#000000")
    f6.config(bg="#CECCBE", fg="#000000")
    f7.config(bg="#CECCBE", fg="#000000")
#For changing the background color of the window, labels etc.
def cldk():
    root.config(bg="#2B2B2B")
    c1.config(bg="#2B2B2B")
    c2.config(bg="#2B2B2B")
    c3.config(bg="#2B2B2B")
    c4.config(bg="#2B2B2B")
    el.config(bg="#2B2B2B")
    tl.config(bg="#2B2B2B")
    f.config(bg="#2C3539")
    cl.config(bg="#2C3539",fg="white")
    c.config(bg="#2C3539")
    text.config(bg="#2C3539",fg="#ffffff")
    btp.config(bg="#666666",fg="#FFFFFF")
    lf.config(bg="#2C3539",fg="#a0d2eb")
    f1.config(bg="#2B2B2B",fg="#CECCBE")
    f2.config(bg="#2B2B2B",fg="#CECCBE")
    f3.config(bg="#2B2B2B",fg="#CECCBE")
    f4.config(bg="#2B2B2B",fg="#CECCBE")
    f5.config(bg="#2B2B2B",fg="#CECCBE")
    f6.config(bg="#2B2B2B",fg="#CECCBE")
    f7.config(bg="#2B2B2B",fg="#CECCBE")
#For changing the selection of radio buttons:
def clk():
    r2.config(value=0)
    r1.config(value=1)
#For changing the selection of radio buttons:
def cdk():
    r2.config(value=1)
    r1.config(value=0)
#For clearing the text entered by the user in the entry box
def clr():
    ety.delete(0,"end")
#For clearing the text in the entry box,text box,output box:
def cla():
    ans=messagebox.askquestion("Confirm Clear", "It clears the 'Saved Data' \n But don't worry the Data is stored")
    if ans=="yes":
        ety.delete(0,"end")
        txt.delete(0,"end")
        text.delete(0,"end")
    else:
        return
#For getting the text in the entry box and output box:
def cpy():
    global cp,x,y
    try:
        word=en.get()
        if word=="":
            e="No word is entered"
            er.delete(0,"end")
            er.insert("end",e)
        else:
            x=word
            y=speech
            cp=x+" = "+y+"\n"
            return cp
    except NameError:
        e="No word is entered/translated"
        er.delete(0,"end")
        er.insert("end",e)
#For inserting the copied text into the text box and inserting the values into the database table:
def pst():
    try:
        text.insert("end",cp)
        form = "insert into words (Enteredtext,Translatedtext) values(%s,%s)"
        mems = [(x, y)]
        mycursor.executemany(form, mems)
        mydb.commit()
    except NameError:
        e="No word is copied"
        er.delete(0,"end")
        er.insert("end",e)
#For deleting the previously stored data in the database table:
def dlt():
    ans=messagebox.askquestion("Warning","Permenantly deletes all the Stored Data",default="no",icon="warning")
    if ans=="yes":
        text.delete(0,"end")
        mysql = "TRUNCATE TABLE Words"
        mycursor.execute(mysql)
        mydb.commit()
    else:
        return
#For inserting the previously stored data into the textbox:
def shw():
    text.delete(0, "end")
    mycursor.execute("select * from words")
    myres = mycursor.fetchall()
    i=1
    for r in myres:
        row=str(i)+'.'+r[0]+'='+r[1]
        text.insert("end",row)
        i=i+1
#For creating a popup window:
def abt():
    win=Toplevel()
    win.title("About")
    win.geometry("400x150")
    win.resizable(False, False)
    win.iconbitmap(r'2.ico')
    w=Label(win,text="Translator",font=("Calibri",20,"bold"),width=10)
    w.pack(pady=10)
    c=Label(win,text='Created on "20th of October 2020"',font=("Arial",15))
    c.pack()
    b=Label(win,text=("Created by 1.Sk.Md Reyaz \n \t   2.G.Mallikarjun \n          3.K.Bavish"),font=("Arial",10))
    b.pack()
#For making the window into Fullscreen mode:
def clf():
    root.attributes("-fullscreen",True)
#For Exiting the Fullscreen mode:
def cle():
    root.attributes("-fullscreen",False)
#For Creating menu buttons at the top:
mb=Menu(root)                                     
root.config(menu=mb)                                 
#To create a new menu button "File" in the toplevel menu
f1=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")             #tearoff is used to remove the dashed line in the list of commands
mb.add_cascade(label="File",menu=f1)
#To add list of commands to the menu button
f1.add_command(label="Show",command=shw)
f1.add_command(label="Delete",command=dlt)
f1.add_command(label="Exit",command=ext)
#To create a new menu button "Edit" in the toplevel menu
f2=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="Edit",menu=f2)
#To add list of commands to the menu button
f2.add_command(label="Copy",command=cpy)
f2.add_command(label="Save",command=pst)
#To create a new menu button "View" in the toplevel menu
f3=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="View",menu=f3)
#To add list of commands to the menu button
f3.add_command(label="Full Screen",command=clf)
f3.add_command(label="Exit Full Screen",command=cle)
#To create a new menu button "Run" in the toplevel menu
f4=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="Run",menu=f4)
#To add list of commands to the menu button
f4.add_command(label="Translate",command=trans)
f4.add_separator()                                                  #add_separator is used to add a line between the list of commands
f4.add_command(label="Speak",command=speak)
#To create a new menu button "Tools" in the toplevel menu
f5=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="Tools",menu=f5)
#To add list of commands to the menu button
f5.add_command(label="Clear",command=clr)
f5.add_command(label="Clear all",command=cla)
#To create a new menu button "Options" in the toplevel menu
f6=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="Options",menu=f6)
#To add list of commands to the menu button
f6.add_command(label="Ligth Mode",command=lambda : [cllk(),clk()])
f6.add_separator()
f6.add_command(label="Dark Mode",command=lambda : [cldk(),cdk()])
#To create a new menu button "Help" in the toplevel menu
f7=Menu(mb,tearoff=False,bg="#CECCBE",fg="#000000")
mb.add_cascade(label="Help",menu=f7)
#To add a command to the menu button
f7.add_command(label="About",command=abt)
f=Frame(root,bg="#4c5f7a",borderwidth=8,relief=GROOVE)                          #To create a frame named f in the root window, GROOVE is used to give styling to the frame
f.pack(side=TOP,fill=X,pady=1)
lf=Label(f,text="Welcome To Translator",bg="#4c5f7a",fg="#001f3f",font="Arial 15 italic bold")              #To create a label in the frame f
lf.pack()
c=Frame(root,bg="#4c5f7a",borderwidth=8,relief=GROOVE)                                      #To create a frame named c in the root window, GROOVE is used to give styling to the frame
c.pack(side=LEFT,fill=Y,padx=5)
btp=Button(c,text="Save",font="Arial 10 bold",bg="#FFCCFF",command=pst)                    #To create a button for inserting the copied text into the listbox and in the file
btp.pack(side=BOTTOM,fill=X,pady=1)
cl=Label(c,text="Saved Data:",fg="black",bg="#4c5f7a",font=("Arial",15,"bold"))            #To create a label above the listbox
cl.pack()
sx=Scrollbar(c,orient=HORIZONTAL)                       #To create a horizontal scroll bar xview
sx.pack(side=BOTTOM,fill=X)
sy=Scrollbar(c)                                         #To create a vertical scroll bar for yview
sy.pack(side=RIGHT,fill=Y)
text=Listbox(c,font="Arial 12",fg="#000000",bg="#4c5f7a",width=15,height=30,xscrollcommand=sx.set,yscrollcommand=sy.set)     #To create a listbox in which the pasted text will appear,(.set) is used to set the scroll bar where we leave it
text.pack()
sx.config(command=text.xview)                                           #To set the scrollbars command to xview
sy.config(command=text.yview)                                           #To set the scrollbars command to yview
c1=Frame(root,bg="#CECCBE",height=200,width=250)                #To create a frame named c1 in the root window
c1.pack(fill=X)
c2=Frame(root,bg="#CECCBE",height=200,width=250)                #To create a frame named c2 in the root window
c2.pack(fill=X,pady=1)
c3=Frame(root,bg="#CECCBE",height=200,width=250)                #To create a frame named c3 in the root window
c3.pack(fill=X)
el=Label(c1,text="Enter text:",font=("Times new roman",30,"bold"),fg="blue",bg="#CECCBE",height=2,width=12)     #To create a label before the entry box
el.pack(side=LEFT,pady=2,padx=2)
btc=Button(c1,text="Clear",font="Arial 10 bold",bg="orange",command=clr)            #To create a button to clear the text enter by user in the entry box
btc.pack(side=RIGHT,padx=10)
ety=Entry(c1,textvariable=en,width=20,font=("Calibri",15),bg="#7FDBFF",borderwidth=5)       #To create a entry box where user can enter the text
ety.pack(side=RIGHT,padx=20)
tb=Button(c2,text="Translate",font=("Arial",10,"bold"),fg="#e2ebf0",bg="blue",command=trans,height=3,width=25,activebackground="#6699FF")   #To create a button to translate the text entered by the user
tb.pack(side=LEFT,pady=5,padx=50)
sb=Button(c2,text="Speak",font=("Arial",10,"bold"),fg="#000000",bg="yellow",command=speak,height=3,width=25,activebackground="#FFFF99")     #To create a button to speak the translated text
sb.pack(side=RIGHT,padx=50)
tl=Label(c3,text="Translated text:",font=("Times new roman",30,"bold"),fg="green",bg="#CECCBE",height=2,width=12)   #To create a label before the output box
tl.pack(side=LEFT,pady=2,padx=2)
btc=Button(c3,text="Copy",font="Arial 10 bold",bg="orange",command=cpy)                #To create a button to copy the text
btc.pack(side=RIGHT,padx=10)
txt=Listbox(c3,height=1,width=20,font=("Calibri",15),bg="#7FDBFF",borderwidth=5)       #To create a box where translated text will appear
txt.pack(side=RIGHT,padx=20)
bte=Button(root,text="Exit",font=("Arial",10,"bold"),bg="red",fg="#EEEEEE",command=ext,height=2,width=20)   #To create a button to exit in the window when clicked on it
bte.pack()
c4=Frame(root,height=100,bg="#CECCBE")      #To create a frame named c4 in root window
c4.pack(side=BOTTOM,fill=X,pady=15,padx=10)
r1=Radiobutton(c4,text="Dark Mode",value=1,variable=i,command=cldk)         #To create a radiobutton for darkmode
r1.pack(side=RIGHT)
r2=Radiobutton(c4,text="Light Mode",value=0,variable=i,command=cllk)        #To create a radiobutton for lightmode
r2.pack(side=RIGHT,padx=5)
erl=Label(c4,text="Error:",bg="#5EFB6E")    #To create a label named Error
erl.pack(side=LEFT)
er=Listbox(c4,height=1,width=30)            #To create a listbox in which the errors will be displayed
er.pack(side=LEFT)
root.protocol("WM_DELETE_WINDOW",ext)               #Protocol method to get alert while closing the window
root.mainloop()
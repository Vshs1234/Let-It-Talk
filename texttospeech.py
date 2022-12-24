from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
ar=Tk()
ar.title("TextToSpeech-BY VSHarshaS")
ar.resizable(False,False)
ar.wm_iconbitmap("favicon.io")
ar.geometry("900x500")
ar.configure(bg="#305065")

engine=pyttsx3.init()
def talk():
    text=textfield.get(1.0,END)
    genderval=gender.get()
    speedval=speed.get()
    voices=engine.getProperty('voices')

    def settingvoice():
        if genderval=='Male':
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if text:
        if speedval=="Fast":
            engine.setProperty('rate',250)
            settingvoice()
        elif speedval=='Normal':
            engine.setProperty('rate',150)
            settingvoice()
        else:
            engine.setProperty('rate',60)
            settingvoice()

def save():
    text=textfield.get(1.0,END)
    genderval=gender.get()
    speedval=speed.get()
    voices=engine.getProperty('voices')

    def settingvoice():
        if genderval=='Male':
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'audio.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'audio.mp3')
            engine.runAndWait()
    if text:
        if speedval=="Fast":
            engine.setProperty('rate',250)
            settingvoice()
        elif speedval=='Normal':
            engine.setProperty('rate',150)
            settingvoice()
        else:
            engine.setProperty('rate',60)
            settingvoice()
# frame up
f1=Frame(ar,bg="white",width=900,height=80)
f1.place(x=0,y=0)
mike=PhotoImage(file="mike.png")
Label(f1,image=mike).place(x=280,y=0)
Label(f1,text="Let It Talk!!",bg="#305065",fg="white",font="arial 20 bold").place(x=400,y=20)

f2=Frame(ar,bg="#305065",width=200,height=100)
f2.pack(padx=110,pady=100)
scroll=Scrollbar(f2)
scroll.pack(side=RIGHT,fill=Y)
textfield=Text(f2,font="arial 15",bg="white",relief=GROOVE,width=200,height=200,wrap=WORD,yscrollcommand=scroll.set)
textfield.pack(padx=10,pady=10)
scroll.config(command=textfield.yview)



gender=Combobox(ar,values=['Male','Female'],font="arial 10",state='r',width=10)
gender.place(x=20,y=200)
gender.set("Female")
Label(ar,text="VOICE",font="Lucida 15 italic",bg="#305065",fg="white").place(x=30,y=150)


speed=Combobox(ar,values=['Fast','Normal','Slow'],font="arial 10",state='r',width=10)
speed.place(x=800,y=200)
speed.set("Normal")
Label(ar,text="SPEED",font="Lucida 15 italic",bg="#305065",fg="white").place(x=800,y=150)


images=PhotoImage(file="speaker.png")
b1=Button(ar,text="Speak",compound=LEFT,image=images,width=150,font="lucida 10 bold",command=talk)
b1.place(x=200,y=425,height=50)


images1=PhotoImage(file="download.png")
b2=Button(ar,text="download",compound=LEFT,image=images1,width=150,font="lucida 10 bold",command=save)
b2.place(x=550,y=425,height=50)


ar.mainloop()
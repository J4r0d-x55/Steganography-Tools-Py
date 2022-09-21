from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="black")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="Selectionner une image",
                                      filetype=(("PNG file","*.png"),
                                                ("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image = img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def save():
    secret.save("hidden.png")

image_icon = PhotoImage(file="malvertising.png")
root.iconphoto(False,image_icon)


Label(root,text="CYBERSECURITY",bg="black",fg="white",font="poppins 25 bold").place(x=20,y=20)

f=Frame(root,bd=3,bg="grey",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="grey")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Ubuntu 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3=Frame(root,bd=3,bg="grey",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Ouvrir Image",width=10,height=1,font="Roboto 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Sauvegarder",width=10,height=1,font="Roboto 14 bold",command=save).place(x=180,y=30)
Label(frame2,bg="white",fg="white").place(x=20,y=5)


frame4=Frame(root,bd=3,bg="grey",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Cacher",width=10,height=1,font="Roboto 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Voir",width=10,height=1,font="Roboto 14 bold",command=Show).place(x=180,y=30)
Label(frame4,bg="grey",fg="white").place(x=20,y=5)
root.mainloop()
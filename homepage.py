import sqlite3 as sql
import random
from tkinter import *
import PIL.Image
import tkinter
from PIL import ImageTk, Image
import PIL.Image
import os

a=['movies','fruits','cities','plants','animals']
f=open('E:\\file\\file.txt','w')
f.write(random.choice(a))
f.close()
root = Tk()
background_image=ImageTk.PhotoImage(PIL.Image.open("new.jpg"))
background_label =Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.resizable(False, False)
root.title("WELCOME")
root.geometry('483x500')
#button
x1=Button(root)
photo=PhotoImage(file="start.gif")
x1.config(image=photo,width="160",height="62",command=root.destroy,activebackground="black",bg="black", bd=0)
x1.place(relx=0.56,rely=0.53,x=10, y=100, anchor=NE)
#END button
  #dropsown    
tkvar = StringVar(root)
photo2=PhotoImage(file="image/random.gif")

choices = { 'movies','fruits','cities','plants','animals'}
tkvar.set('random') # set the default option
root.wm_attributes('-fullscreen', True)
root.wm_attributes('-transparent', root['bg'])
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.config(image=photo2,width="170",height="60",activebackground="#800000",bg="black", bd=.5, highlightbackground= "white")

photo2=PhotoImage(file=str("image/"+tkvar.get()+".gif"))
popupMenu.config(image=photo2)
popupMenu.place(relx=0.43,rely=0.56)


def fili(strk):
    f=open('E:\\file\\file.txt','w')
    f.write(strk)
    #print(f.read())
    f.close()
    
def change_dropdown(*args):
    global photo2, popupMenu
    photo2=PhotoImage(file=str("image/"+tkvar.get()+".gif"))
    popupMenu.config(image=photo2,width="170",height="60",activebackground="#800000",bg="black", bd=.5, highlightbackground= "white")
    fili(tkvar.get())
        
tkvar.trace('w', change_dropdown)
root.mainloop()
  #END dropdown
 ##END home page
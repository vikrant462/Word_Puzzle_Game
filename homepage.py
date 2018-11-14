import sqlite3 as sql
import winsound
import random
from tkinter import *
import PIL.Image
import tkinter
from PIL import ImageTk, Image
import PIL.Image
import os

#sound
winsound.PlaySound("game_menu",winsound.SND_ASYNC)
#ENDsound

a=['movies','fruits','cities','plants','animals']
f=open('file.txt','w')
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
x1.place(relx=0.545,rely=0.60,x=10, y=100, anchor=NE)
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
    f=open('file.txt','w')
    f.write(strk)
    #print(f.read())
    f.close()
    
def change_dropdown(*args):
    global photo2, popupMenu
    photo2=PhotoImage(file=str("image/"+tkvar.get()+".gif"))
    popupMenu.config(image=photo2,width="170",height="60",activebackground="#800000",bg="black", bd=.5, highlightbackground= "white")
    fili(tkvar.get())
        
tkvar.trace('w', change_dropdown)
#dropdown1    
tkvar1 = StringVar(root)
photo3=PhotoImage(file="image/easy.gif")

choices1 = { 'easy','hard'}
tkvar1.set('easy') # set the default option
f=open('file1.txt','w')
f.write(tkvar1.get())
f.close()
popupMenu1 = OptionMenu(root, tkvar1, *choices1)
popupMenu1.config(image=photo3,width="155",height="50",activebackground="#800000",bg="black", bd=.5, highlightbackground= "white")

photo3=PhotoImage(file=str("image/"+tkvar1.get()+".gif"))
popupMenu1.config(image=photo3)
popupMenu1.place(relx=0.436,rely=0.64)


def fili1(strk):
    f=open('file1.txt','w')
    f.write(strk)
    f.close()
    
def change_dropdown1(*args):
    global photo3, popupMenu1
    photo3=PhotoImage(file=str("image/"+tkvar1.get()+".gif"))
    popupMenu1.config(image=photo3,width="155",height="50",activebackground="#800000",bg="black", bd=.5, highlightbackground= "white")
    fili1(tkvar1.get())
        
tkvar1.trace('w', change_dropdown1)
root.mainloop()
  #END dropdown
 ##END home page

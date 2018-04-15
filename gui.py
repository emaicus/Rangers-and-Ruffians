from tkinter import *
from tkinter import messagebox
from PIL import ImageTk as itk
from PIL import Image

import os

runpath = os.getcwd()
image_dir = os.path.join(runpath, "images")

root = Tk()
root.geometry("1000x600")

def loadImage(img_name, scale=1):
  img_name = os.path.join(image_dir, img_name)


  image = Image.open(img_name)
  xscale = int(image.size[0] * scale)
  yscale = int(image.size[1] * scale)
  image = image.resize((xscale, yscale), Image.ANTIALIAS)

  photo = itk.PhotoImage(image)
  return photo

def chose_human():
  msg = messagebox.showinfo( "Human", "You chose human!")

img = loadImage("human_male.jpg", scale=.25)
B = Button(root, image =img , command = chose_human)
B.place(x = 50,y = 50)




root.mainloop()
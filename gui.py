import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import messagebox
from PIL import ImageTk as itk
from PIL import Image

import os

runpath = os.getcwd()
image_dir = os.path.join(runpath, "images")
race_dir = os.path.join(image_dir, "races")
female_race_dir = os.path.join(race_dir, "female")
male_race_dir = os.path.join(race_dir, "male")

# root = Tk()
# root.geometry("1000x600")







# def chose_human():
#   msg = messagebox.showinfo( "Human", "You chose human!")

# human_image = loadImage("human_male.jpg", scale=.25)
# # human_image = loadImage("human_male.jpg", scale=.25)
# # human_image = loadImage("human_male.jpg", scale=.25)
# # human_image = loadImage("human_male.jpg", scale=.25)
# # human_image = loadImage("human_male.jpg", scale=.25)

# B = Button(root, image =human_image , command = chose_human)
# B.place(x = 50,y = 50)




# root.mainloop()
player_gender_male = False

def loadImage(image_path, scale=1):
  image = Image.open(image_path)
  xscale = int(image.size[0] * scale)
  yscale = int(image.size[1] * scale)
  #hard coding for now.
  image = image.resize((180, 277), Image.ANTIALIAS)

  out = itk.PhotoImage(image)
  return out

def loadRaceImages(male):
  images = list()
  directory = male_race_dir if male else female_race_dir

  for image in os.listdir(directory):
    #first strip away path, then suffix.
    image_path = os.path.join(directory, image)
    race_name = image.split("/")[-1].split(".")[0]
    # img = loadImage(image, scale=.25)
    images.append((race_name, image_path))
  return images







class RangersClassCreationApp(tk.Tk):
    #initialize the app.
    def __init__(self):
      tk.Tk.__init__(self)
      self._frame = None
      self.switch_frame(StartPage)

    #switch frame destroys the current frame and replaces it with a new one.
    def switch_frame(self, frame_class):
      new_frame = frame_class(self)
      if self._frame is not None:
          self._frame.destroy()
      self._frame = new_frame
      self._frame.pack()

    def setGender(self,male):
      global player_gender_male
      player_gender_male = male
      self.switch_frame(racePage)

    def raceDetails(self, race):
      print(race)


class StartPage(tk.Frame):

  def __init__(self, master):
    #These two lines together are used for resizing.
    tk.Frame.__init__(self, master, height=200, width=400)
    self.pack_propagate(False)

    start_label = tk.Label(self, text="Welcome to Rangers and Ruffians!\nPlease select your character's gender.")
    page_1_button = tk.Button(self, text="Male",
                              command=lambda: master.setGender(male=True))
    page_2_button = tk.Button(self, text="Female",
                              command=lambda: master.setGender(male=False))
    start_label.pack(side="top", fill="x", pady=10)
    page_1_button.pack()
    page_2_button.pack()

class racePage(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self, master)
    txt = "male" if player_gender_male else "female"
    name_image_list = loadRaceImages(player_gender_male)

    #back button
    page_1_label = tk.Label(self, text=txt)
    start_button = tk.Button(self, text="Return to start page",
                             command=lambda: master.switch_frame(StartPage))

    buttons = list()
    grid = tk.Grid()
    label = tk.Label(text="Label 1")
    label.grid(row=0)
    label = tk.Label(text="Label 2")
    label.grid(row=0, column=1)
    label = tk.Label(text="Label 3")
    label.grid(row=1, column=2)
    label = tk.Label(text="Label 4")
    label.grid(row=4, column=3)
    label = tk.Label(text="Label 5")
    label.grid(row=2, column=0)
    # i = 0
    # for name, image_path in name_image_list:
    #   img = loadImage(image_path, scale=.25)
    #   print(name)
    #   B = tk.Button(self, image=img, command=lambda: master.raceDetails(race=name))
    #   B.image = img
    #   B.grid(row=i%3, column=i//3)
    #   print(i//3, i%3)
    #   i+=1
    #   # buttons.append(B)

    start_button.pack()
    page_1_label.pack(side="top", fill="x", pady=10)
    # for button in buttons:
    #   i += 1
    #   button.pack()





    


class PageTwo(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self, master)

    page_2_label = tk.Label(self, text="This is page two")
    start_button = tk.Button(self, text="Return to start page",
                             command=lambda: master.switch_frame(StartPage))
    page_2_label.pack(side="top", fill="x", pady=10)
    start_button.pack()


if __name__ == "__main__":
    app = RangersClassCreationApp()
    app.mainloop()
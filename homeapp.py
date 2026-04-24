from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
from train import *
from test import *


root = Tk()
root.title("TraitPass Speaker Recognition")

window_height = 200
window_width = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

## Resizable Image
image = Image.open(r'bggif/TraitPass_Logo.jpg')
global copy_of_image
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

## Calling training and testing functions
def training():
    Training_file()

def testing():
    Testing_file()

## Adding Buttons
train_button = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",10,'bold italic'), activeforeground="orange", text='Train the machine', padx=6, pady=6, command = training)
train_button.place(relx=0.15, rely=0.75, anchor=CENTER)

test_button = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",10,'bold italic'), text='Test the machine', padx=6, pady=6, command = testing)
test_button.place(relx=0.585, rely=0.75, anchor=CENTER)

quit = Button(root, fg="white", background="green", activebackground="green",font=("Helvetica",10,'bold italic'), text="Quit", command=root.destroy, padx=6, pady=6)
quit.place(relx=0.94, rely=0.75, anchor=CENTER)

root.mainloop()

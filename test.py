from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from record_module import *
from username import *
from db import *

fname = "testfile.wav"

class Testing_file:
    def __init__(self):
        root = Toplevel()
        root.title("TraitPass Speaker Recognition")
        window_height = 200
        window_width = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        ## Resizable Image

        image = Image.open('bggif/TraitPass_Logo.jpg')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding Buttons
        user_label = Label(root, bg="black", fg="white", text="Sign In")
        user_label.config(font=("Courier", 15))
        user_label.place(relx=0.58, rely=0.2, anchor='e')

        user_label = Label(root, bg="black", fg="white", text="Desc: Record is to take one voice input for user verification.")
        user_label.config(font=("Courier", 10))
        user_label.place(relx=0.0, rely=0.95, anchor='w')

        recording_button = Button(root, text="Record", bd=0, bg="black", fg="white", font=("Courier",14),command=record_audio)
        recording_button.place(relx=0.3, rely=0.5, anchor=CENTER)

        play_button = Button(root, text="Play", bd=0, bg="black", fg="white", font=("Courier",14),command=self.audioplay)
        play_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        test_button = Button(root, text="Login", bd=0, bg="black", fg="white", font=("Courier",14),command = self.testaudio)
        test_button.place(relx=0.7, rely=0.5, anchor=CENTER)

        root.mainloop()


    ## Function for resizing the Image

    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo

    def audioplay(self):
        global fname
        play_audio(fname)

    def testaudio(self):
        k = test1()
        recog(k)


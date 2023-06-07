from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from trainrecord import *
from record_module import *
from GMM1 import *

fname = ''

class Training_file:
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

        image = Image.open(r'bggif/TraitPass_Logo.jpg')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        ## Adding TextBoxes
        user_label = Label(root, bg="black", fg="white", text="Sign Up")
        user_label.config(font=("Courier", 15))
        user_label.place(relx=0.55, rely=0.2, anchor='e')

        user_label = Label(root, bg="black", fg="white", text="User name")
        user_label.config(font=("Courier", 10))
        user_label.place(relx=0.25, rely=0.4, anchor='w')

        global v1
        v1 = StringVar()
        user_entry = self.EntryWithPlaceholder(root, "Enter the username","black",textvariable = v1)
        user_entry.place(relx=0.65, rely=0.4, anchor='e')

        user_label = Label(root,bg="black", fg="white", text="Duration(sec)")
        user_label.config(font=("Courier", 10))
        user_label.place(relx=0.18, rely=0.5, anchor='w')

        user_label = Label(root, bg="black", fg="white", text="Description: username is file name for saving 5 voice entries.")
        user_label.config(font=("Courier", 10))
        user_label.place(relx=0.0, rely=0.95, anchor='w')

        global v2
        v2 = StringVar()
        user_entry = self.EntryWithPlaceholder(root, "Enter the Duration","black",textvariable = v2)
        user_entry.place(relx=0.65, rely=0.5, anchor='e')

        ## Adding Buttons
        rec_button = Button(root, text="Record", bd=0, bg="black", fg="white", font=("Courier",13),command = self.reco)
        rec_button.place(relx=0.35, rely=0.65, anchor=CENTER)

        play_button = Button(root, text="Play", bd=0, bg="black", fg="white", font=("Courier",13),command = self.play)
        play_button.place(relx=0.50, rely=0.65, anchor=CENTER)

        train_button = Button(root, text="Train", bd=0, bg="black", fg="white", font=("Courier",13),command = self.train)
        train_button.place(relx=0.65, rely=0.65, anchor=CENTER)

        root.mainloop()


    ## Class for a placeholder

    class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',textvariable = None):
            super().__init__(master,textvariable = textvariable)

            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.foc_in)
            self.bind("<FocusOut>", self.foc_out)

            self.put_placeholder()

        def put_placeholder(self):
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

        def foc_in(self, *args):
            if self['fg'] == self.placeholder_color:
                self.delete('0', 'end')
                self['fg'] = self.default_fg_color

        def foc_out(self, *args):
            if not self.get():
                self.put_placeholder()
                
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

    ## Recording

    def reco(self):
            global fname
            global v1,v2
            try:
                    fname = testr(str(v1.get()),float(v2.get()))
            except:
                    fname = testr(v1.get())

    ## Playing the last recorded

    def play(self):
            global fname
            play_audio(fname)

    def train(self):
            global v1
            traine(v1.get())

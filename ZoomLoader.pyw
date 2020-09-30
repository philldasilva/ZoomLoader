import subprocess
from tkinter import *

FIREFOX = "C:/Program Files/Mozilla Firefox/firefox"

CLASS1LINK = ""
CLASS2LINK = ""
CLASS3LINK = ""
CLASS4LINK = ""
CLASS5LINK = ""
CLASS6LINK = ""

# Create the window and set it up
class Window(Frame):

    # Define the settings upon init
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class
        Frame.__init__(self, master)                 

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to run the init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ZoomLoader")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        ButtonClass1 = Button(self, text="", width=28, height=6, command=self.class_1)
        ButtonClass2 = Button(self, text="", width=28, height=6, command=self.class_2)
        ButtonClass3 = Button(self, text="", width=28, height=6, command=self.class_3)
        ButtonClass4 = Button(self, text="", width=28, height=6, command=self.class_4)
        ButtonClass5 = Button(self, text="", width=28, height=6, command=self.class_5)
        ButtonClass6 = Button(self, text="", width=28, height=6, command=self.class_6)

        # placing the button on my window
        ButtonClass1.grid(row=0, column=0)
        ButtonClass2.grid(row=0, column=1)
        ButtonClass3.grid(row=1, column=0)
        ButtonClass4.grid(row=1, column=1)
        ButtonClass5.grid(row=2, column=0)
        ButtonClass6.grid(row=2, column=1)

    # Open up firefox with the correct zoom link when the button is pressed
    def class_1(self):
        subprocess.call([FIREFOX, CLASS1LINK])

    def class_2(self):
        subprocess.call([FIREFOX, CLASS2LINK])

    def class_3(self):
        subprocess.call([FIREFOX, CLASS3LINK])

    def class_4(self):
        subprocess.call([FIREFOX, CLASS4LINK])
    
    def class_5(self):
        subprocess.call([FIREFOX, CLASS5LINK])

    def class_6(self):
        subprocess.call([FIREFOX, CLASS6LINK])


### MAIN ###

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  
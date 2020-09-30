import subprocess
import tkinter as tk

FIREFOX = "C:/Program Files/Mozilla Firefox/firefox"

# Create the window and set it up
class Button:

    row = 0

    #Creation of init_window
    def __init__(self, name, link):

        # Configuring Rows / Columns
        tk.Grid.rowconfigure(root, Button.row, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)
        
        self.button = tk.Button(root, text=name, compound=tk.LEFT, command=lambda: gotoLink(link))
        self.button.grid(sticky="nswe")
        Button.row += 1

        # Button Command
        def gotoLink(link):
            subprocess.call([FIREFOX, link])

        """# Creating new buttons
        n = len(LINKS)
        j = 0
        for i in range(n):
            e = button(self, text=list(LINKS.keys())[i], command=lambda : gotoLink(list(LINKS.values())[i]))
            e.grid(row=i, column=j)"""

        
def getClasses():
    numClasses = int(input("Enter number of classes to add: "))

    links = []

    for i in range(numClasses):
        name = input("Enter name for class " + str(i) + ": ")
        link = input("Enter link for class " + str(i) + ": ")
        links.append([name, link])

    return(links)


### MAIN ###

# Need to set up the GUI here...

links = getClasses()

# Start up the GUI
root = tk.Tk()
root.title("ZoomLoader")
# Set size of the window
root.geometry("400x300")

for l in links:
    b = Button(*l)

root.mainloop()  
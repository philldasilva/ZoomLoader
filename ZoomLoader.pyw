import subprocess
from os import path
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

        
def getClasses():
    numClasses = int(input("Enter number of classes to add: "))

    links = []

    for i in range(numClasses):
        name = input("Enter name for class " + str(i+1) + ": ")
        link = input("Enter link for class " + str(i+1) + ": ")
        links.append([name, link])

    return(links)

def checkConfig():

    links = []

    # Check if there is a config file already, if not, set one up
    if path.exists("config.txt"):
        with open("config.txt", "r") as fr:
            for line in fr:
                current = line[:-1]  
                links.append([i for i in list(current.split("\t")) if i])
    else:
        links = getClasses()
        with open("config.txt", "w") as fw:
            for link in links:
                for kv in link:
                    fw.write('%s\t' % kv)
                fw.write('\n')

    return(links)

### MAIN ###

links = checkConfig()

# Start up the GUI
root = tk.Tk()
root.title("ZoomLoader")
# Set size of the window
root.geometry("400x300")

for l in links:
    b = Button(*l)

root.mainloop()  
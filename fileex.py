import os
import subprocess
from tkinter import *
files = os.listdir("exec")
#print(files)
allFiles = []
class GUI:

    def start(self):

        root = Tk()
        root.resizable(0,0)
        def print_ingredients(*args):
            global allFiles
            allFiles = []
            values = [(ingredient, var.get()) for ingredient, var in data.items()]
            for k in values:
                for i in k:
                    i = str(i)
                    i[:-1]
                    if i == "1" or i==1:
                        allFiles.append(k[0])
                        print(allFiles)
            root.quit()
        data = {}



        mb = Menubutton(root, text="List of programs:", relief=RAISED,font=("Calibri",30),padx=20,pady=10)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        for ingredient in files:
            var = IntVar()
            mb.menu.add_checkbutton(label=ingredient, variable=var)
            data[ingredient] = var  # add IntVar to the dictionary

        btn = Button(root, text="Submit", command=print_ingredients,font=("Calibri",30),padx=20,pady=10)
        btn.pack()

        mb.pack()

        root.mainloop()

        labels = []  # creates an empty list for your labels

if __name__ != '__main__':
    os.kill(os.getpid(),9)
GUI().start()
for file in allFiles:
    #subprocess.call(f"exec/{file}",shell=False)
    os.startfile(f"exec\\{file}")


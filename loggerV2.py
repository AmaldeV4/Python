import tkinter as tk
from datetime import datetime

now = datetime.now()
dt = now.strftime('%d/%m/%y %H:%M:%S')


window = tk.Tk()
window.title("Dev")
window.geometry("200x100")

nameEntry = tk.Entry(font=('Cascadia mono', 12), bg="#2d333d")
nameEntry.pack()

def myClick():
    myLabel = tk.Label(font=('Cascadia mono', 12), text="Hello " + nameEntry.get() + "! Logged")
    myLabel.pack()
    f = open("file.txt", "a")
    f.write("\n" + nameEntry.get() + " logged at " + dt)
    f.close()
    nameEntry.delete(0, tk.END)
    exit()


myButton = tk.Button(font=('Cascadia mono', 12), text="Enter", command=myClick)
myButton.pack()


window.mainloop()
